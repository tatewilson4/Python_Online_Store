from django.shortcuts import render
from django.views.generic import ListView
from . import models
from products.models import Product


class Home(ListView):
    model = Product
    template_name = 'products/home.html'


def base(request):
    return render(request, 'base.html')
