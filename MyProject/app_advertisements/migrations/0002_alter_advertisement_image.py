# Generated by Django 4.2.6 on 2023-11-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(upload_to='advertisement', verbose_name='Изображение'),
        ),
    ]
