from django.urls import path

from main.apps import MainConfig
from main.views import index, show_product, contacts, categories

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', categories, name='categories'),
    path('product/<int:pk>', show_product, name='product'),
]
