from django.shortcuts import render
from store.models import *


def store(request):
    products = Product.objects.all()
    return render(request, 'store/store.html', context={"products": products})


def cart(request):
    return render(request, 'store/cart.html', context={})


def checkout(request):
    return render(request, 'store/checkout.html', context={})
