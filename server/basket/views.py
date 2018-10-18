from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Basket
from products.models import Product

def basket_view(request):
    context = {}
    return render(request, 'basket/view.html', context)

def basket_add(request, pk):
    product = get_object_or_404(Product, id=pk)
    old_busket_item = Basket.objects.filter(user=request.user, product=product)


    if old_busket_item:
        print(type(old_busket_item))
        print(old_busket_item)
        old_busket_item[0].quantity += 1
        old_busket_item[0].save()
    else:
        new_busket_item = Basket(user=request.user, product=product)
        new_busket_item.quantity += 1
        new_busket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket_remove(request):
    context = {}
    return render(request, 'basket/view.html', context)
