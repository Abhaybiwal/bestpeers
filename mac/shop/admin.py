from django.contrib import admin

from .models import Product,ProductCategory,Contact,Cart

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Contact)
admin.site.register(Cart)
