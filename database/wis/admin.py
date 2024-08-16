from django.contrib import admin
from .models import Product , Product2 , Product3,Product4

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)

admin.site.register(Product, ProductAdmin )
admin.site.register(Product2, ProductAdmin )
admin.site.register(Product3, ProductAdmin )
admin.site.register(Product4, ProductAdmin )
