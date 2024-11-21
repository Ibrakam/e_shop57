from django import forms
# Импортируем готовую модель пользователя
from django.contrib.auth.models import User
# Импортируем готовый модуль для создания полтьзователя
from django.contrib.auth.forms import UserCreationForm


# Форма для регистрации
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Форма для логина
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
