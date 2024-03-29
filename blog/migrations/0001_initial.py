# Generated by Django 4.2.7 on 2024-01-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('content', models.CharField(max_length=50, verbose_name='содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='material/', verbose_name='изображение')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('publication', models.BooleanField(default=True, verbose_name='признак публикации')),
                ('count', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блог',
                'ordering': ('title',),
            },
        ),
    ]
