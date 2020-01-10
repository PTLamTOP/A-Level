from django import forms
from django.contrib.auth.models import User
from .models import Article

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['text']



