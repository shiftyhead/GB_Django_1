from django.urls import path, re_path
from products.views.categories import (
    category_create, category_detail, category_list,# category_update
)
app_name = 'categories'

urlpatterns = [
    path('create/', category_create, name='create'),
    path('<int:pk>/', category_detail, name='detail'),
    path('', category_list, name='list'),
    # path('update/<int:pk>/', category_update, name='update'),
]
