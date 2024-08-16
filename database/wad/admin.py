from django.contrib import admin
from .models import Brand  ,Brand2 , Brand3,Brand4 ,Brand5

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded') 
    search_fields = ('name', 'description')
    list_filter = ('name',)

@admin.register(Brand2)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded') 
    search_fields = ('name', 'description')
    list_filter = ('name',)

@admin.register(Brand3)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded') 
    search_fields = ('name', 'description')
    list_filter = ('name',)

@admin.register(Brand4)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded') 
    search_fields = ('name', 'description')
    list_filter = ('name',)

@admin.register(Brand5)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded') 
    search_fields = ('name', 'description')
    list_filter = ('name',)