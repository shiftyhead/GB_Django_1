from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from products.models import ProductCategory, Product
from products.forms import CategoryModelForm
from basket.models import Basket
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def index(request):
    return render(request, 'categories/list.html')

class CategoryGenericList(ListView):

    model = ProductCategory
    template_name = 'categories/list.html'
    context_object_name = 'items'

class CategoryGenericDetail(DetailView):

    model = ProductCategory
    template_name = 'categories/detail.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = context.get('object')
        context[self.context_object_name] = instance.product_set.all()
        return context

class CategoryGenericCreate(CreateView):

    model = ProductCategory
    form_class = CategoryModelForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:list')

class CategoryGenericUpdate(UpdateView):

    model = ProductCategory
    form_class = CategoryModelForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:list')

class CategoryGenericDelete(DeleteView):
    model = ProductCategory
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:list')

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
