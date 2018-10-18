from django.urls import path, re_path
from products.views.products import (
    product_create, product_update, product_detail, product_list
)

app_name = 'products'

urlpatterns = [
    path('create/', product_create, name='create'),
    path('<int:pk>/', product_detail, name='detail'),
    path('update/<int:pk>/', product_update, name='update'),
    path('', product_list, name='list'),
]
