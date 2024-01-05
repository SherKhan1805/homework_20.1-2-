from django.db import models
from main.utils import NULLABLE
from users.models import User


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='название', unique=True, **NULLABLE)
    description = models.CharField(max_length=200, verbose_name='описание')
    image = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name='категория', **NULLABLE) #удалить строчку
    price = models.IntegerField(verbose_name='цена за покупку')
    create_date = models.DateTimeField(verbose_name='дата создания')
    edit_date = models.DateTimeField(verbose_name='дата последнего изменения')
    category1 = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category', verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='автор', null=True, blank=True)

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
        return f'{self.name}. {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Contact(models.Model):
    """
    Модель для контактов
    """
    name = models.CharField(max_length=50, verbose_name='название организации')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField()

    def __str__(self):
        return f'{self.name}. {self.email}. {self.phone_number}. {self.address}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('name',)


class Blog(models.Model):
    """
    Модель для блога
    """
    title = models.CharField(max_length=50, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', blank=True, null=True)
    content = models.CharField(max_length=50, verbose_name='содержимое')
    image = models.ImageField(upload_to='material/', verbose_name='изображение', **NULLABLE)
    create_date = models.DateTimeField(auto_now_add=True)
    publication = models.BooleanField(default=True, verbose_name='признак публикации')
    count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блог'
        ordering = ('title',)


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='id_product')
    number_version = models.IntegerField(verbose_name='номер версии', **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='наименование')
    is_active_version = models.BooleanField(default=True, verbose_name='применить версию')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
