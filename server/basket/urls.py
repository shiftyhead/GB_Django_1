from django.urls import path, re_path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_view, name='view'),
    re_path(r'^add/(?P<pk>\d+)/$', views.basket_add, name='add'),
    re_path(r'^remove/(?P<pk>\d+)/$', views.basket_remove, name='remove'),


]
