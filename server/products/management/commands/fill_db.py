from django.core.management.base import BaseCommand
from ...models import ProductCategory, Product
from authapp.models import ShopUser
from images.models import Image
from django.conf import settings
import json, os

JSON_PATH = os.path.join(settings.STATIC_ROOT, 'products/json/')

def loadFromJSON(file_name):
    with open(JSON_PATH + file_name + '.json', 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = loadFromJSON('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = loadFromJSON('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category

            image_name = product['image']
            _image = Image.objects.get(name=image_name)
            product['image'] = _image

            new_product = Product(**product)
            new_product.save()

        ShopUser.objects.all().delete()
        super_user = ShopUser.objects.create_superuser('django',
            'django@geekshop.local', 'geekbrains', age=33)
