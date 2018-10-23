"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from products.endpoints.products import ProductViewSet


router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', include('products.urls.categories')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('api/', include(router.urls)),
    path('basket/', include('basket.urls', namespace='basket')),
    path('subd/', include('adminapp.urls', namespace='subd')),
    path('', include('products.urls.products')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
