from django.shortcuts import render


def catalog(request):
    d1 = {
        'name': 'dv-506',
        'type': 'magnitola'
    }
    d2 = {
        'name': '1000w',
        'type': 'dinamiki'
    }
    d3 = {
        'name': '7 цветов'
    }
    products = [d1, d2, d3]
    return render(request, 'catalog/catalog.html', {'products': products})
