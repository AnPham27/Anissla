from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name ="store"),
    path('tops/', views.tops, name="tops"),
    path('bottoms/', views.bottoms, name="bottoms"),
    path('shoes/', views.shoes, name="shoes"),
    path('accessories/', views.accessories, name="accessories"),
    path('cart/', views.cart, name ="cart"),
    path('checkout/', views.checkout, name ="checkout"),
]