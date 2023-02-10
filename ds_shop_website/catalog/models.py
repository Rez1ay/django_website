from django.db import models
from django.urls import reverse


class Product(models.Model):
    brand = models.CharField('Бренд', max_length=50)
    model = models.CharField('Модель', max_length=100)
    photo = models.ImageField('Фото', upload_to='photo')
    info = models.TextField('Описание')
    price = models.CharField('Цена', max_length=20)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('card', kwargs={'card_id': self.model})
