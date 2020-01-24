from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, FormView
from note.models import Note, Author
from .forms import NoteForm, TokenForm
from django.urls import reverse

from uuid import uuid4
from django.shortcuts import redirect

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AuthorRegisterForm

from django.core.mail import send_mail





# NOTE views
class SharedNoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'note/shared_notes.html'
    context_object_name = 'shared_notes'
    login_url = 'login'
    # ordering = ['-created_at']
    # paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_shared=True)
        return queryset


class UnShareNoteView(UpdateView):
    Model = Note
    fields = ['is_shared']
    queryset = Note.objects.all()

    def get_success_url(self):
        return reverse('note:shared-note-list')

    def form_valid(self, form):
        instance = form.instance
        instance.is_shared = False
        instance.save()
        return super().form_valid(form)


class ShareNoteView(UpdateView):
    Model = Note
    fields = ['is_shared']
    queryset = Note.objects.all()

    def get_success_url(self):
        return reverse('note:note-list')

    def form_valid(self, form):
        instance = form.instance
        instance.is_shared = not instance.is_shared
        instance.save()
        return super().form_valid(form)


class NoteListView(ListView):
    model = Note
    template_name = 'note/note_list.html'
    context_object_name = 'notes'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('text')
        if query:
            search_result = Note.objects.filter(text__icontains=query)
            context.update({'search_result': search_result})
        context.update({'note_form': NoteForm})
        return context


class NoteCreateView(CreateView):
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('note:note-list')


class NoteDeleteView(DeleteView):
    model = Note
    context_object_name = 'note'

    def get_success_url(self):
        return reverse('note:note-list')


# USER views
class CustomLoginView(LoginView):
    template_name = 'user/login.html'

    def get_success_url(self):
        user = self.request.user
        time_until_block = None
        subject = f"{user.username}, please confirm your email!"
        message = f"{user.username}, your account would be blocked in {2} days {3} hours."
        result = send_mail(subject, message, 'lam.djangotestmail@gmail.com', [user.email])
        return reverse('note:note-list')


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'note/note_list.html'
    login_url = 'login'


class RegistrationView(CreateView):
    template_name = 'user/register.html'
    http_method_names = ['get', 'post']
    form_class = AuthorRegisterForm

    def get_success_url(self):
        return reverse('login')

    def form_valid(self, form):
        form.instance.token = uuid4()
        form.save()
        return super().form_valid(form)


class ConfirmEmail(FormView):
    # Model = Author
    # fields = ['token']
    form_class = TokenForm
    template_name = 'user/confirm_email.html'
    # queryset = Author.objects.all()

    def form_valid(self, form):
        author_instance = Author.objects.get(id=self.kwargs['pk'])
        token = form.cleaned_data['token']
        if author_instance.token == token:
            author_instance.email_confirmed = True
            author_instance.save()
            return super().form_valid(form)
        return redirect('confirm-email')

    def get_success_url(self):
        return reverse('note:note-list')

    # def form_valid(self, form):
    #     instance = form.instance
    #     token = form.cleaned_data['token']
    #     if instance.token == token:
    #         instance.email_confirmed = True
    #         form.save()
    #         return super().form_valid(form)
    #     return redirect('confirm-email')