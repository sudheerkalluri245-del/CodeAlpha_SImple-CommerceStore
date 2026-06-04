from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product, Cart, Order


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration Successful")
        return redirect('login')

    return render(request, 'register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        messages.error(request, "Invalid Credentials")

    return render(request, 'login.html')


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    return render(
        request,
        'cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )