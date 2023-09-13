from django.shortcuts import render
from django.db.models import Sum

from myapp5.models import Product

# Счиатем сумму тремя разными способами (через БД, через функцию во view, через шаблон модели (внутри неё)):

def total_in_db(request): # считаем сумму через запрос к БД (aggregate)
    total = Product.objects.aggregate(Sum('quantity')) 
    context = { 
        'title': 'Общее количество посчитано в базе данных', 
        'total': total, 
        } 
    return render(request, 'myapp6/total_count.html', context)


def total_in_view(request): # считаем сумму с помощью инструментов языка Python (sum) во view
    products = Product.objects.all() 
    total = sum(product.quantity for product in products) 
    context = { 
        'title': 'Общее количество посчитано в представлении', 
        'total': total, 
        } 
    return render(request, 'myapp6/total_count.html', context)


def total_in_template(request): #считаем сумму через сойство самой модели (сама логика нахождения суммы будет в специально созданном свойстве модели (в виде метода))
     context = { 
         'title': 'Общее количество посчитано в шаблоне', 
         'products': Product, 
         } 
     return render(request, 'myapp6/total_count.html', context)

