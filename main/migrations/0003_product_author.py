# Generated by Django 4.2.7 on 2023-12-31 13:22

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blog_contact_alter_product_name_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name=users.models.User),
        ),
    ]
