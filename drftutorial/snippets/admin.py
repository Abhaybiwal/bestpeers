from django.contrib import admin
from .models import Book,UserProfile,Album,Artist,Track
# Register your models here.

admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Track)