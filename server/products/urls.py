from django.urls import path, re_path
from . import views

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', views.product_detail, name='detail'),
    re_path(r'^category/(?P<pk>\d+)/$', views.product_list, name='category'),
    path('', views.product_list, name='list'),
]
