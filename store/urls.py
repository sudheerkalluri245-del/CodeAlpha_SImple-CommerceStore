from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path(
        'product/<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'cart/',
        views.cart_view,
        name='cart'
    ),

    path(
        'add-to-cart/<int:product_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),
]