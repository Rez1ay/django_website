from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from .forms import *


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


class RegUser(CreateView):
    form_class = RegUserForm
    template_name = 'main/reg.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'main/profile.html')
    else:
        return redirect('/login', permanent=True)
