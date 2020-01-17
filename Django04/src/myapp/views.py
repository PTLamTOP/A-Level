from django.urls import reverse
from django.views.generic import ListView, FormView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .models import Article, Author, Comment
from .forms import ArticleForm, UserRegisterForm, CreateCommentForm

from django.contrib.auth.mixins import LoginRequiredMixin

"""
def get_context_data(self, object_list=None, **kwargs):
    context = super().get_context_data(object_list=None, **kwargs)
    context.update({'comment_create': CreateCommentForm,
                    })
    return context
    """
class UpdateCommentStatusVIew(UpdateView):
    model = Comment
    fields = ['is_active']
    template_name = 'myapp/update_comment.html'

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.object.article.id})


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'myapp/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = context.get('object')
        comments_active = Comment.objects.filter(article=article, is_active=True)
        context.update({'comment_create': CreateCommentForm,
                        'comments_active': comments_active})
        return context


class CreateCommentView(CreateView):
    model = Comment
    fields = ['user', 'article', 'text', 'comment']
    template_name = 'myapp/create_comment.html'

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.request.POST.get('article')})


class CommentDetailView(DetailView):
    model = Comment
    context_object_name = 'comment'
    template_name = 'myapp/comment_detail.html'


class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'myapp/delete_comment.html'
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.object.article.id})


class UpdateCommentVIew(UpdateView):
    model = Comment
    fields = ['text']
    template_name = 'myapp/update_comment.html'

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.object.article.id})


class ChangingPasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'myapp/change_pass.html'

    def get_success_url(self):
        return reverse('index')


class RegistrationView(FormView):
    template_name = 'myapp/register.html'
    http_method_names = ['get', 'post']
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# QUESTION
class SearchResultList(ListView):
    model = Article
    ordering = ['-created_at']
    template_name = 'myapp/search.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(text__icontains=self.request.GET.get('text'),
                                   author=self.request.GET.get('author'))
        return queryset


class ArticleListView(ListView):
    model = Article
    template_name = 'myapp/index.html'
    context_object_name = 'articles'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'article_create': ArticleForm})
        return context


class ArticleCreateView(CreateView):
    model = Article
    fields = ['author', 'text', 'genre']
    template_name = 'myapp/article_create.html'

    def get_success_url(self):
        return reverse('index')


class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse('index')


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'myapp/logout.html'
    login_url = 'login'







"""
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


# пример реализации login в Django функциональный подход
def login_view(request):

    if request.method == 'POST':
        # .POST хранит данные отправленной формы в виде словаря
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'myapp/index.html', {'user': user})
        else:
            return HttpResponse('Login wrong data!')

    else:
        form = LoginForm()

    return render(request, 'myapp/login.html', {'form': form})


# пример реализации login в Django функциональный подход
def logout_view(request):
    logout(request)
    return render(request, 'myapp/logout.html')
"""