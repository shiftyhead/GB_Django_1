from django.shortcuts import render, get_object_or_404
# import json
from .models import ProductCategory, Product

def product_list(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    if pk:
        category = ProductCategory.objects.filter(id=pk).order_by('name')
        products = Product.objects.filter(category__id=pk).order_by('name')
        context = {
            'title': title,
            'links_menu': links_menu,
            'categories': category,
            'items': products
        }

    else:
        products = Product.objects.all().order_by('name')
        context = {
            'title': title,
            'links_menu': links_menu,
            'items': products
        }
    return render(request, 'products/list.html', context)


def product_detail(request, pk):

    # with open('products/static/products/json/items.json') as json_file:
        # context = json.load(json_file)

    # obj = Product.objects.get(id=pk)
    obj = {'instance': get_object_or_404(Product, id=pk)}

    return render(request, 'products/detail.html', obj)
