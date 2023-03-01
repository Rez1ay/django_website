# Generated by Django 4.1.5 on 2023-03-01 08:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Информация о пользователе', 'verbose_name_plural': 'Информация о пользователях'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='user-photo', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=150, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(default=20, validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(99)], verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Man', 'Мужской'), ('Woman', 'Женский')], max_length=8, verbose_name='Пол'),
        ),
    ]