from django.db import models
from django.urls import reverse


class Product(models.Model):
    brand = models.CharField('Бренд', max_length=50)
    model = models.CharField('Модель', max_length=100)
    info = models.TextField('Описание')

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('card', kwargs={'card_id': self.pk})
