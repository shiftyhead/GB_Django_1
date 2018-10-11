from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from products.models import ProductCategory, Product
from django.http import HttpResponse
from basket.models import Basket
from products.forms import ProductModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView

class ProductGenericList(ListView):

    model = Product
    template_name = 'products/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links_menu'] = ProductCategory.objects.all()
        return context


class ProductGenericDetail(DetailView):

    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'instance'

class ProductGenericCreate(CreateView):

    model = Product
    form_class = ProductModelForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:list')

class ProductGenericUpdate(UpdateView):

    model = Product
    form_class = ProductModelForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:list')


def product_list(request):
    title = 'продукты'
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


def product_detail(request, pk):

    obj = {'instance': get_object_or_404(Product, id=pk)}

    return render(request, 'products/detail.html', obj)

def product_create(request):

    success_url = reverse_lazy('products:list')

    form = ProductModelForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():

            form.save()

            return redirect(success_url)

    return render(request, 'products/create.html', {'form': form})


def product_update(request, pk):

    success_url = reverse_lazy('products:list')

    obj = get_object_or_404(Product, id=pk)

    form = ProductModelForm(instance=obj)

    if request.method == 'POST':

        form = ProductModelForm(
            request.POST,
            instance=obj
        )

        if form.is_valid():

            form.save()

            return redirect(success_url)

    return render(request, 'products/create.html', {'form': form})
