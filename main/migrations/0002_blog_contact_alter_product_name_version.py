# Generated by Django 4.2.7 on 2023-12-31 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
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
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название организации')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='название'),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_version', models.IntegerField(blank=True, null=True, verbose_name='номер версии')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('is_active_version', models.BooleanField(default=True, verbose_name='применить версию')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='id_product')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
