from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from user.forms import UserLoginForm, UserRegisterForm


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print(form)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            print(user)
            login(request, user)
            return redirect('login')
        else:
            form = UserRegisterForm()
            return render(request, 'registration.html',
                          {"form": form})
    else:
        form = UserRegisterForm()
        return render(request, 'registration.html',
                      {"form": form})


# Логика для Login
def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            form = UserLoginForm()
            return render(request, "login.html", {"form": form})
    else:
        form = UserLoginForm()
        return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("about")
