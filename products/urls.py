from django.urls import path
from . import views
from products import views
from . views import ProductDetail
from cart.views import add_to_cart, remove_from_cart, CartView, decreaseCart
app_name= 'mainapp'



urlpatterns = [
    path('', views.featured_list, name='home'),
    path('cart/', CartView, name='cart-home'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
    path('product/<slug>/', ProductDetail.as_view(), name='product'),
    path('decrease-cart/<slug>', decreaseCart, name='decrease-cart'),

]
