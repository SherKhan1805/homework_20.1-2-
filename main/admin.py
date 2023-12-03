from django.contrib import admin

from main.models import Product, Category, Contact, Blog


# Register your models here.


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'image', 'create_date')
    search_fields = ('title', 'description',)


# регистрация модели контактов
admin.site.register(Contact)