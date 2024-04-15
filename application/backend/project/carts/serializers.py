from rest_framework import serializers
from carts.models import Cart, CartItem
from orders.models import Order

class CartItemSerializer(serializers.ModelSerializer):
    '''
    The serializer responsible for generating a JSON response for cart items.
    '''
    product_id = serializers.IntegerField(source="product.id", read_only=True)
    product = serializers.CharField(source="product.name")
    price = serializers.FloatField(source="product.price", read_only=True)
    image = serializers.FileField(source="product.image")
    class Meta:
        model = CartItem
        fields = ["product_id", "product", "price", "image", "quantity"]

class ManageCartItemSerializer(serializers.ModelSerializer):
    '''
    The serializer responsible for validating a JSON body when creating or updating a cart item.
    '''
    quantity = serializers.IntegerField()
    class Meta:
        model = CartItem
        fields = ["product", "quantity"]

class CartSerializer(serializers.ModelSerializer):
    '''
    The serializer responsible for generating a JSON response for user's carts.
    '''
    user = serializers.CharField(source="user.username")
    items = CartItemSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = ["confirmed", "user", "items"]

class ManageCartSerializer(serializers.ModelSerializer):
    '''
    The serializer responsible for validating a JSON body when creating or updating a cart.
    '''
    class Meta:
        model = CartItem
        fields = "__all__"

class CheckOutSerializer(serializers.ModelSerializer):
    '''
    The serializer responsible for validating a JSON body when creating an order.
    '''
    postal_code = serializers.RegexField("^[1-9][0-9]{5}$")
    class Meta:
        model = Order
        fields = "__all__"
        