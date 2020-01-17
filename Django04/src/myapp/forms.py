from django import forms
from django.contrib.auth.models import User
from .models import Article, Comment
from django.contrib.auth.forms import UserCreationForm


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'article', 'text', 'comment', 'is_active']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'text', 'genre']


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


