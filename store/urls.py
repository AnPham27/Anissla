from django.urls import path, include   
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.store, name ="store"),
    path('products/', views.products, name="products"),
    path('cart/', views.cart, name ="cart"),
    path('checkout/', views.checkout, name ="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('confirmation/', views.confirmation, name="confirmation"),
    path('support/', views.support, name="support")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
