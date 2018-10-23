from django.urls import path, re_path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.BasketGenericList.as_view(), name='list'),
    path('add/<int:pk>/', views.basket_add, name='add'),
    path('delete/<int:pk>/', views.BasketGenericDelete.as_view(), name='delete'),


]
