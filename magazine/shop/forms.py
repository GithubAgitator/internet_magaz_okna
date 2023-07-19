from django import forms
from django.contrib.auth.models import User

from .models import *
from django.contrib.auth.forms import UserCreationForm


class SubscribersForm(forms.ModelForm):
    email = models.EmailField()
    name = models.CharField(max_length=100)

    class Meta:
        model = Subscriber
        exclude = ['']


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class FeedBackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': "Ваше имя"
        })
    )
    email = forms.CharField(
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': "Ваша почта"
        })
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control md-textarea',
            'id': 'message',
            'rows': 2,
            'placeholder': "Ваше сообщение"
        })
    )

class ZamerUserForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'ФИО',
            'placeholder': "ФИО"
        })
    )
    number = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'Ваш номер телефона',
            'placeholder': "Ваш номер телефона"
        })
    )

    adress = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'Ваш адрес',
            'placeholder': "Ваш адрес"
        })
    )


