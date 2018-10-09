from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from products.models import ProductCategory, Product
from products.forms import CategoryModelForm
from basket.models import Basket

def category_create(request):

    success_url = reverse_lazy('products:list')

    form = CategoryModelForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():

            form.save()

            return redirect(success_url)

    return render(request, 'products/create.html', {'form': form})

def category_list(request):
    title = 'категории'
    links_menu = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        print(basket)

    products = Product.objects.all().order_by('name')
    context = {
        'title': title,
        'links_menu': links_menu,
        'items': products,
        'basket': basket,
    }
    return render(request, 'products/list.html', context)


def category_detail(request, pk):

    obj = {
    'instance': get_object_or_404(ProductCategory, id=pk),
    'items': Product.objects.filter(category=pk)
    }

    return render(request, 'products/category.html', obj)
