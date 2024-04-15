from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    '''
    The serializer responsible for generating a JSON response based on product data.
    '''
    class Meta:
        model = Product
        fields = "__all__"
        
