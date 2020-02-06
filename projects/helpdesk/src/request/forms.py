from django import forms
from .models import Request, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class RequestCreateForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['subject', 'text', 'importance']

