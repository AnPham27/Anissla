from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def store(request):
    products = Product.objects.all()[0:6]
    context = {'products': products}
    return render(request, 'store/store.html',context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def tops(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/tops.html', context)

def bottoms(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/bottoms.html', context)

def shoes(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/shoes.html', context)

def accessories(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/accessories.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
