from django.urls import path
from . import views
from . views import Home
from cart.views import add_to_cart, remove_from_cart, CartView
app_name= 'mainapp'


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cart/', CartView, name='cart-home'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
]
