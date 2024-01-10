from django.db import models
from main.utils import NULLABLE


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
