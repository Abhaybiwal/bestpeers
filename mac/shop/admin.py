from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Product,ProductCategory,Contact,Cart, CustomUser


# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

# admin.site.unregister(User)
admin.site.register(CustomUser, UserAdmin)

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Contact)
admin.site.register(Cart)
