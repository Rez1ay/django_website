from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    USER_GENDER = (
        ('Man', 'Мужской'),
        ('Woman', 'Женский'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField('Фото', upload_to='user-photo', blank=True)
    address = models.CharField('Адрес', max_length=150, blank=True)
    age = models.PositiveIntegerField('Возраст', validators=[MinValueValidator(12), MaxValueValidator(99)], default=0)
    gender = models.CharField('Пол', max_length=8, choices=USER_GENDER, blank=True)

    class Meta:
        verbose_name = 'Информация о пользователе'
        verbose_name_plural = 'Информация о пользователях'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
