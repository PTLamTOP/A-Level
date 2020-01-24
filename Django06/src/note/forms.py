from django import forms
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from .models import Author


class TokenForm(forms.Form):
    token = forms.CharField(max_length=50)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']


class AuthorRegisterForm(UserCreationForm):
    class Meta:
        model = Author
        fields = ['username', 'email', 'password1', 'password2']