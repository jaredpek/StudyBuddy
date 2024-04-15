from rest_framework import serializers
from carts.models import Cart, CartItem
from orders.models import Order

class CartItemSerializer(serializers.ModelSerializer):
    '''
    The serializer responsible for generating a JSON output for a cart item.
    '''
    product = serializers.CharField(source="product.name")
    image = serializers.FileField(source="product.image")
    price = serializers.FloatField(source="product.price", read_only=True)
    class Meta:
        model = CartItem
        fields = ["product", "image", "price", "quantity"]

class CartSerializer(serializers.ModelSerializer):
    '''
    The serializer responsible for generating a JSON output for a user's cart with required details.
    '''
    items = CartItemSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = ["items"]

class OrderSerializer(serializers.ModelSerializer):
    '''
    The serializer responsible for generating a JSON output for a user's order.
    '''
    cart = CartSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ["id", "order_status", "date_ordered", "cart", "address", "postal_code", "total"]
