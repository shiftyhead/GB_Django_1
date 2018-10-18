from django.urls import path, re_path
from products.views.categories import (
    CategoryGenericList, CategoryGenericDetail,
    CategoryGenericCreate, CategoryGenericUpdate, CategoryGenericDelete,
    category_create, category_detail, category_list, index
)
app_name = 'categories'

urlpatterns = [
    path('create/', CategoryGenericCreate.as_view(), name='create'),
    path('delete/<int:pk>/', CategoryGenericDelete.as_view(), name='delete'),
    path('update/<int:pk>/', CategoryGenericUpdate.as_view(), name='update'),
    path('<int:pk>/', CategoryGenericDetail.as_view(), name='detail'),
    path('', index, name='index'),

]
