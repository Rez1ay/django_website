from django.shortcuts import render
from .models import Product


def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog/catalog.html', {'products': products})


def card(request, card_id):
    products = Product.objects.filter(id=card_id)
    return render(request, 'catalog/card.html', {'products': products})
