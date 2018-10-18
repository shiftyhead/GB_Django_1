from django.urls import path, re_path
from products.views.products import (
    ProductGenericList, ProductGenericDetail, ProductGenericCreate, ProductGenericUpdate,
    ProductGenericDelete,
    product_create, product_update, product_detail, product_list
)

app_name = 'products'
endpointspatterns = [
    path('api/products/', product_list, name='list_api')
]
urlpatterns = [
    path('create/', ProductGenericCreate.as_view(), name='create'),
    path('<int:pk>/', ProductGenericDetail.as_view(), name='detail'),
    path('update/<int:pk>/', ProductGenericUpdate.as_view(), name='update'),
    path('', ProductGenericList.as_view(), name='list'),
    path('delete/<int:pk>/', ProductGenericDelete.as_view(), name='delete'),

] + endpointspatterns
