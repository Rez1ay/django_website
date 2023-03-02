# Generated by Django 4.1.5 on 2023-03-02 10:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_profile_options_remove_profile_product-photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(99)], verbose_name='Возраст'),
        ),
    ]