from django.urls import path
from . import views


urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<str:card_id>', views.card, name='card')
]
