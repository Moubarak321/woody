from django.contrib import admin
from .models import Category, Product
# Register your models here.

# class AdminProduct(admin.ModelAdmin)
class AdminProduct(admin.ModelAdmin):
    list_display= ('name', 'price', 'category')


class AdminCategory(admin.ModelAdmin):
    list_display= ('product')

admin.site.register(Product, AdminProduct)
admin.site.register(Category)