from django.urls import path
from . import views


urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<int:card_id>', views.card, name='card')
]