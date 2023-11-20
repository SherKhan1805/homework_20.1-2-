from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.CharField(max_length=200, verbose_name='описание')
    image = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    create_date = models.DateTimeField(verbose_name='дата создания')
    edit_date = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.CharField(max_length=200, verbose_name='описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)