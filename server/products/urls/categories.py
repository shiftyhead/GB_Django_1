from django.urls import path, re_path
from products.views.categories import (
    CategoryGenericList, CategoryGenericDetail,
    CategoryGenericCreate, CategoryGenericUpdate,
    category_create, category_detail, category_list,# category_update
)
app_name = 'categories'

urlpatterns = [
    path('create/', CategoryGenericCreate.as_view(), name='create'),
    path('<int:pk>/', CategoryGenericDetail.as_view(), name='detail'),
    path('', CategoryGenericList.as_view(), name='list'),
    path('update/<int:pk>/', CategoryGenericUpdate.as_view(), name='update'),
]
