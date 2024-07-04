# urls.py
from django.urls import path
from .views import *

app_name='shop'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('tracker/', TrackerView.as_view(), name='tracker'),
    path('search/', SearchView.as_view(), name='search'),
    path('products/<int:myid>/', ProductView.as_view(), name='product'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('submit_data/', submit_data,name="submit_data"),


]
