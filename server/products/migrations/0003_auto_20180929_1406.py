# Generated by Django 2.1.1 on 2018-09-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180929_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='snippet',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
    ]