# urls.py
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


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
    path('update_cart/', update_cart,name='update_cart'),
    path('cartitems/',CartItems.as_view(), name='cartitems'),
    path('contact/thanks/', ThanksView.as_view(), name='thanks'),
    
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='shop/logged_out.html'), name='logout'),

    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='shop/password_change_done.html'), name='password_change_done'),
    
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='shop/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
