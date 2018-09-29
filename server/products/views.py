from django.shortcuts import render, get_object_or_404
# import json
from .models import ProductCategory, Product

def product_list(request):

    # with open('products/static/products/json/items.json') as json_file:
    #     context = json.load(json_file)
    # context = {'items':[i['title'] for i in context['items']]}

    context = {'items': Product.objects.all()}

    return render(request, 'products/list.html', context)

def product_detail(request, pk):

    # with open('products/static/products/json/items.json') as json_file:
        # context = json.load(json_file)

    # obj = Product.objects.get(id=pk)
    obj = {'instance': get_object_or_404(Product, id=pk)}

    return render(request, 'products/detail.html', obj)
