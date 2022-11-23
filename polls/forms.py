from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import inlineformset_factory
from polls.models import AdvUser


class UserRegisterForm(UserCreationForm):
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    middle_name = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    checkbox = forms.CharField(label='Согласие на обработку персональных данных')

    class Meta:
        model = AdvUser
        fields = ('last_name', 'first_name', 'middle_name', 'username', 'email', 'password1', 'password2', 'checkbox')