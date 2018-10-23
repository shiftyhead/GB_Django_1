from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import JsonResponse

from products.models import Product


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
