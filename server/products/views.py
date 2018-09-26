from django.shortcuts import render
import json

def product_list(request):

    with open('products/static/products/json/items.json') as json_file:
        context = json.load(json_file)
    context = {'items':[i['title'] for i in context['items']]}

    return render(request, 'products/list.html', context)

def product_detail(request, pk):

    with open('products/static/products/json/items.json') as json_file:
        context = json.load(json_file)

    return render(request, 'products/detail.html', {'product_title': context['items'][pk]['title'],
                                                    'product_text': context['items'][pk]['text']})
