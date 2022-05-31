
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('plus', views.cart_plus, name='cart_plus'),
    path('minus', views.cart_minus, name='cart_minus'),
    path('delete', views.cart_pak, name='cart_pak'),
    # path('add/<int:id_pro>', AddToCartView, name="addtocartview"),
]

