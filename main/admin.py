from django.contrib import admin

from main.models import Product, Category

# Register your models here.


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)
