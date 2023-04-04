from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.store, name ="store"),
    path('tops/', views.tops, name="tops"),
    path('bottoms/', views.bottoms, name="bottoms"),
    path('shoes/', views.shoes, name="shoes"),
    path('accessories/', views.accessories, name="accessories"),
    path('cart/', views.cart, name ="cart"),
    path('checkout/', views.checkout, name ="checkout"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
