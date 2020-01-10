from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class StudentForm(forms.Form):
    SEX_CHOICES = (
        (1, _('male')),
        (2, _('female')),
    )

    ENGLISH_LEVEL_CHOICES = (
        (1, _("Not selected")),
        (2, _("A")),
        (3, _("A1")),
        (4, _("A2")),
        (5, _("B")),
        (6, _("B1")),
        (7, _("B2")),
        (8, _("C")),
        (9, _("C1")),
        (10, _("C2")),
        (11, _("C3")),
    )

    name = forms.CharField(label='name', max_length=100, required=True)
    sex = forms.ChoiceField(label='sex', choices=SEX_CHOICES, required=True)
    age = forms.IntegerField(label='age', required=True)
    english_level = forms.ChoiceField(label='english_level', choices=ENGLISH_LEVEL_CHOICES, required=True)


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']



