from django.contrib import admin

from .models import Category, Image, Blog

admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Blog)
