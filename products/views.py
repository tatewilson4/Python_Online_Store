from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['mainimage', 'name', 'slug', 'category', 'preview_text', 'detail_text', 'price']

class ProductDetail(LoginRequiredMixin, DetailView):
	model = Product


def featured_list(request, template_name='products/home.html'):
    product = Product.objects.all()
    data = {}
    data['object_list'] = product
    return render(request, template_name, data)

def product_list(self):
    product = Product.objects.order_by('-id')[0:10]
    data = {}
    data['object_list'] = product
    return render(request, template_name, data)
