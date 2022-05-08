from django.contrib import admin
from .models import Product, Category ,Register_table, Order

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','category']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Register_table)
admin.site.register(Order)
