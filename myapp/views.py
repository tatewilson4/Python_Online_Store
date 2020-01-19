from django.shortcuts import render
from django.views.generic import ListView
from . import models
from myapp.models import Product


class Home(ListView):
    model = Product
    template_name = 'myapp/home.html'


def base(request):
    return render(request, 'base.html')
