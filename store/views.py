from django.shortcuts import render

# Create your views here.

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def tops(request):
    context = {}
    return render(request, 'store/tops.html', context)

def bottoms(request):
    context = {}
    return render(request, 'store/bottoms.html', context)

def shoes(request):
    context = {}
    return render(request, 'store/shoes.html', context)

def accessories(request):
    context = {}
    return render(request, 'store/accessories.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
