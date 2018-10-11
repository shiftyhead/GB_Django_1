from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import JsonResponse

from products.models import ProductCategory


def categories_list(request):
    query = get_list_or_404(ProductCategory)
    data = map(lambda itm: {
        'name': itm.name,
        'snippet': itm.snippet,
    }, query)
    return JsonResponse({'results': list(data), 'count': len(query)})
