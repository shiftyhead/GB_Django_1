from django.urls import path, include
from . import views
from django.urls import reverse_lazy
from products.views.products import ProductGenericList, ProductGenericDetail, ProductGenericUpdate, ProductGenericDelete
app_name = 'subd'
success_url = reverse_lazy('subd:subd_products')
urlpatterns = [
    path('products/',
        ProductGenericList.as_view(template_name='adminapp/list.html'),
        name='subd_products'
    ),
    path('products/<int:pk>/',
        ProductGenericDetail.as_view(),
        name='product_detail'
    ),
    path('products/update/<int:pk>/',
        ProductGenericUpdate.as_view(success_url=success_url),
        name='product_update'
    ),
    path('products/delete/<int:pk>/',
        ProductGenericDelete.as_view(success_url=success_url),
        name='product_delete'
    ),

]
