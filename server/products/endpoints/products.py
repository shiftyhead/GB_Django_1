from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def product_list(request):
    query = get_list_or_404(Product)
    data = map(lambda itm: {
        'name': itm.name,
        'category': itm.category.name,
        'image': itm.image.value.url,
        'snippet': itm.snippet,
        'cost': itm.cost
    }, query)
    return JsonResponse({'results': list(data), 'count': len(query)})
