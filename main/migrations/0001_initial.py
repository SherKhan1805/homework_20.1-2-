# Generated by Django 4.2.7 on 2023-11-21 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('description', models.CharField(max_length=200, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('description', models.CharField(max_length=200, verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='изображение')),
                ('category', models.CharField(max_length=50, verbose_name='категория')),
                ('price', models.IntegerField(verbose_name='цена за покупку')),
                ('create_date', models.DateTimeField(verbose_name='дата создания')),
                ('edit_date', models.DateTimeField(verbose_name='дата последнего изменения')),
                ('category1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='main.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('name',),
            },
        ),
    ]
