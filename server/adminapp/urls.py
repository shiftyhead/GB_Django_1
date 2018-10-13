from django.urls import path, include
from . import views
from django.urls import reverse_lazy
from products.views.products import (
    ProductGenericList, ProductGenericDetail,
    ProductGenericUpdate, ProductGenericDelete
)
from products.views.categories import (
    CategoryGenericCreate, CategoryGenericUpdate, CategoryGenericDelete,
    CategoryGenericList, CategoryGenericDetail,
)

app_name = 'subd'
products_success_url = reverse_lazy('subd:products')
categories_success_url = reverse_lazy('subd:categories')
urlpatterns = [
    path('products/',
        ProductGenericList.as_view(template_name='adminapp/products/list.html'),
        name='products'
    ),
    path('products/<int:pk>/',
        ProductGenericDetail.as_view(),
        name='product_detail'
    ),
    path('products/update/<int:pk>/',
        ProductGenericUpdate.as_view(success_url=products_success_url),
        name='product_update'
    ),
    path('products/delete/<int:pk>/',
        ProductGenericDelete.as_view(success_url=products_success_url),
        name='product_delete'
    ),
    path('categories/',
        CategoryGenericList.as_view(template_name='adminapp/categories/list.html'),
        name='categories'
    ),
    path('categories/<int:pk>/',
        CategoryGenericDetail.as_view(),
        name='category_detail'
    ),
    path('categories/update/<int:pk>/',
        CategoryGenericUpdate.as_view(success_url=categories_success_url),
        name='category_update'
    ),
    path('categories/delete/<int:pk>/',
        CategoryGenericDelete.as_view(success_url=categories_success_url),
        name='category_delete'
    ),
]
