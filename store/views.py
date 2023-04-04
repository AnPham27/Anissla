from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

#home page
def store(request):
    context = {}
    return render(request, 'store/store.html',context)

def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'store/cart.html', context)

def tops(request):
    tops = Top.objects.all()
    context = {'tops':tops}
    return render(request, 'store/tops.html', context)

def bottoms(request):
    bottoms = Bottom.objects.all()
    context = {'bottoms':bottoms}
    return render(request, 'store/bottoms.html', context)

def shoes(request):
    shoes = Shoe.objects.all()
    context = {'shoes':shoes}
    return render(request, 'store/shoes.html', context)

def accessories(request):
    accessories = Accessory.objects.all()
    context = {'accessories':accessories}
    return render(request, 'store/accessories.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
