from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'category', 'image', 'snippet', 'cost']


    def get_category(self, obj):
        return obj.category.name

    def get_image(self, obj):
        return obj.image.value.url
