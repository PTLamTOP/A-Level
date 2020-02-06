from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

from django.views.generic import ListView, UpdateView, CreateView, View, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Request, Refusal, Approval, Denial
from .forms import RequestCreateForm, CommentForm

from .serializer import RequestSerializer
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class RequestRetrieveViewSet(viewsets.GenericViewSet,
                             mixins.ListModelMixin):
    """
    Serializer for retrieving Requests
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['importance', ]
    permission_classes = [IsAuthenticated & IsAdminUser]

"""
ADMIN FUNCTIONALITIES
"""
class RequestApproveView(UserPassesTestMixin, View):
    """
    Admin can approve only requests which have status:
        - in progress
        - or repeated request.
    Actions:
        1) test
        2) if ok -> change status of request to 'Approved'
        3) Create Approval object to Request object.
    """
    request_obj = None

    def post(self, request, *args, **kwargs):
        self.request_obj.status = 'AP'
        if hasattr(self.request_obj, 'refusal'):
            self.request_obj.refusal.delete()
        self.request_obj.save()
        approval_obj = Approval(request=self.request_obj)
        approval_obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def test_func(self):
        self.request_obj = Request.objects.get(pk=self.kwargs.get('pk'))
        valid_status = ['IP', 'RR']
        if self.request.user.is_superuser:
            if self.request_obj.status in valid_status:
                return True


class RequestRefuseView(UserPassesTestMixin, CreateView):
    """
    Admin can refuse only a request which have status 'In Progress'.
    Actions:
        1) test
        2) if ok -> change status of request to 'Refused'
        3) Create Refusal object to Request object.
    """
    model = Refusal
    fields = ['comment']
    template_name = 'refusal/create.html'
    request_obj = None

    def form_valid(self, form):
        self.request_obj.status = 'RF'
        self.request_obj.save()
        form.instance.request = self.request_obj
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('requests:request-list')

    def test_func(self):
        self.request_obj = Request.objects.get(pk=self.kwargs.get('pk'))
        valid_status = ['IP']
        if self.request.user.is_superuser:
            if self.request_obj.status in valid_status:
                return True


class RequestDeclineView(UserPassesTestMixin, View):
    """
    Admin can decline only a request which have status 'Repeated Request'.
    Actions:
        1) test
        2) if ok -> change status of request to 'Declined'
        3) Delete Refusal object.
        4) Create Denial object
    """
    request_obj = None

    def post(self, request, *args, **kwargs):
        self.request_obj.status = 'DC'
        self.request_obj.save()
        denial_obj = Denial(request=self.request_obj)
        denial_obj.comment = self.request_obj.refusal.comment
        denial_obj.save()
        self.request_obj.refusal.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def test_func(self):
        self.request_obj = Request.objects.get(pk=self.kwargs.get('pk'))
        valid_status = ['RR']
        if self.request.user.is_superuser:
            if self.request_obj.status in valid_status:
                return True


class ReRequestListView(UserPassesTestMixin, ListView):
    """
    list of all request with status 'Repeated Request'.
    """
    model = Request
    template_name = 're-request/list.html'
    context_object_name = 'rerequests'
    paginate_by = 4
    queryset = Request.objects.filter(status='RR')

    def test_func(self):
        if self.request.user.is_superuser:
            return True

"""
USER FUNCTIONALITIES
"""
class ReRequestView(UserPassesTestMixin, View):
    """
    User can resend a request which was refused again if:
        - request has status 'Refused';
        - user is owner of the request.
    Actions:
        1) test
        2) if ok -> change status of request to 'Repeated Request'
    """
    request_obj = None

    def post(self, request, *args, **kwargs):
        self.request_obj = Request.objects.get(pk=kwargs.get('pk'))
        self.request_obj.status = 'RR'
        self.request_obj.save()
        return redirect(request.META.get('HTTP_REFERER'))

    def test_func(self):
        self.request_obj = Request.objects.get(pk=self.kwargs.get('pk'))
        valid_status = ['RF']
        if self.request.user == self.request_obj.user:
            if self.request_obj.status in valid_status:
                return True


class RequestCreateView(CreateView):
    """
    User create new Request object.
    """
    form_class = RequestCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return str(self.object.get_absolute_url())


class RequestUpdateView(UserPassesTestMixin, UpdateView):
    """
    User can update new requests which have status 'in progress' if he is owner of the request.
    """
    model = Request
    fields = ['text', 'importance']
    template_name = 'request/update.html'
    context_object_name = 'request'

    def test_func(self):
        request_obj = Request.objects.get(pk=self.kwargs.get('pk'))
        valid_status = ['IP']
        if self.request.user == request_obj.user:
            if request_obj.status in valid_status:
                return True


"""
USER AND ADMIN FUNCTIONALITIES
"""
class RequestListView(ListView):
    """
    List of all requests for admin and user.
    If user - show all users' requests excluding status 'repeated request'.
    if admin - show all requests which are in progress.
    """
    model = Request
    template_name = 'request/list.html'
    context_object_name = 'requests'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            queryset = queryset.filter(status='IP')
        else:
            queryset = queryset.filter(user=self.request.user).exclude(status='RR')
        return queryset

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context.update({'request_create_form': RequestCreateForm, })
        return context


class RequestDetailView(UserPassesTestMixin, DetailView):
    """
    Only owner of a request or admin can see detail page of request.
    """
    model = Request
    template_name = 'request/detail.html'
    context_object_name = 'request'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context.update({'comments': self.object.comments.all(),
                        'comment_form': CommentForm, })
        return context

    def test_func(self):
        request_obj = Request.objects.get(pk=self.kwargs.get('pk'))
        if self.request.user == request_obj.user or self.request.user.is_superuser:
            return True


class CommentCreateView(UserPassesTestMixin, CreateView):
    """
    Only owner of a request or admin can comment to a request
    and status of request is 'In Progress'.
    """
    form_class = CommentForm
    request_obj = None

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.request = self.request_obj
        return super().form_valid(form)

    def get_success_url(self):
        return str(self.request.META.get('HTTP_REFERER'))

    def test_func(self):
        self.request_obj = Request.objects.get(pk=self.kwargs.get('pk'))
        valid_status = ['IP']
        if self.request.user == self.request_obj.user or self.request.user.is_superuser:
            if self.request_obj.status in valid_status:
                return True
