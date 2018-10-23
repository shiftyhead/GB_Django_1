from django.urls import path, re_path
from products.views.products import (
    ProductGenericList, ProductGenericDetail, ProductGenericCreate, ProductGenericUpdate,
    ProductGenericDelete,
    product_create, product_update, product_detail, product_list, products_pages
)

app_name = 'products'
endpointspatterns = [
    path('api/products/', product_list, name='list_api')
]
urlpatterns = [
    path('<int:page>/', products_pages, name='list'),
    path('create/', ProductGenericCreate.as_view(), name='create'),
    path('products/<int:pk>/', ProductGenericDetail.as_view(), name='detail'),
    path('update/<int:pk>/', ProductGenericUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProductGenericDelete.as_view(), name='delete'),

] + endpointspatterns
