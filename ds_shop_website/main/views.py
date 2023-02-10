from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


class RegUser(CreateView):
    form_class = RegUserForm
    template_name = 'main/reg.html'
    success_url = reverse_lazy('home')
