from django.urls import path
from . import views

app_name='shop'
urlpatterns = [
    path('',views.index,name='ShopHome'),
    path('about/',views.about,name='About'),
    path('contact/',views.contact,name='ContactUs'),
    path('tracker/',views.tracker,name='TrackingStatus'),
    path('search/',views.search,name='Search'),
    path('products/<int:myid>/',views.prodeuct_view,name='ProductView'),
    path('checkout/',views.checkout,name='Checkout'),

]