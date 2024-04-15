from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from project.response import Response as Result
from carts.models import Cart, CartItem
from carts.serializers import CartSerializer, ManageCartItemSerializer, CheckOutSerializer

def get_or_create(object, **kwargs):
    '''
    The function responsible for getting or creating a specific object based on provided kwargs.
    '''
    try:
        return object.objects.get(**kwargs)
    except:
        return object.objects.create(**kwargs)

class CartView(APIView):
    '''
    The view for cart-related APIs.
    - GET /api/cart/ (Retrieve a user's cart)
    - POST /api/cart/ (User adds a product to his cart)
    - PUT /api/cart/ (User updates the quantity of a product in his cart)
    '''
    permission_classes = [IsAuthenticated, ]
    queryset = Cart.objects.all()
    
    def get(self, request):
        '''
        The function responsible for retrieving all the items in the user's cart.
        '''
        result = Result()
        cart = get_or_create(Cart, user=request.user, confirmed=False)
        result.result.update(CartSerializer(cart).data)
        total = 0
        for item in result.result["items"]:
            item["subtotal"] = item["price"] * item["quantity"]
            total += item["subtotal"]
        result.set_messages("total", total)
        return Response(result.result, status.HTTP_200_OK)
    
    def post(self, request):
        '''
        The function responsible for adding a new product to the user's cart.
        '''
        result = Result()
        serializer = ManageCartItemSerializer(data=request.data)
        if not serializer.is_valid():
            for error in serializer.errors:
                result.set_error(error, serializer.errors[error], as_list=False)
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        if serializer.validated_data["quantity"] <= 0:
            result.set_error("quantity", "This field must be a positive integer.")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        cart = get_or_create(Cart, user=request.user, confirmed=False)
        cart_item = get_or_create(CartItem, cart=cart, product=serializer.validated_data["product"])
        try:
            cart_item.quantity += serializer.validated_data["quantity"]
            cart_item.save()
            result.set_message("add_to_cart", code="success")
            return Response(result.result, status.HTTP_200_OK)
        except:
            result.set_error("add_to_cart", code="error")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        '''
        The function responsible for updating the quantity of a product in the user's cart.
        '''
        result = Result()
        serializer = ManageCartItemSerializer(data=request.data)
        if not serializer.is_valid():
            for error in serializer.errors:
                result.set_error(error, serializer.errors[error], as_list=False)
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        cart = get_or_create(Cart, user=request.user, confirmed=False)
        cart_item = get_or_create(CartItem, cart=cart, product=serializer.validated_data["product"])
        quantity = serializer.validated_data["quantity"]
        if quantity <= 0:
            try:
                cart_item.delete()
                result.set_message("remove_from_cart", code="success")
                return Response(result.result, status.HTTP_200_OK)
            except:
                result.set_error("remove_from_cart", code="error")
                return Response(result.result, status.HTTP_400_BAD_REQUEST)
        try:
            cart_item.quantity = quantity
            cart_item.save()
            result.set_message("update_cart", code="success")
            return Response(result.result, status.HTTP_200_OK)
        except:
            result.set_error("update_cart", code="error")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)

class CheckOutView(APIView):
    '''
    The view for cart checkout API.
    - POST /api/cart/checkout/ (User checks out his cart and creates a new order)
    '''
    permission_classes = [IsAuthenticated, ]
    queryset = Cart.objects.all()
    
    def post(self, request):
        '''
        The function responsible for creating a new order and clearing the user's existing cart.
        '''
        result = Result()
        try:
            cart = Cart.objects.get(user=request.user, confirmed=False)
        except:
            result.set_error("cart", "Cart is currently empty.")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        request.data.update({"user": request.user.pk, "cart": cart.pk, "total": cart.get_total()})
        serializer = CheckOutSerializer(data=request.data)
        if not serializer.is_valid():
            for error in serializer.errors:
                result.set_errors(error, serializer.errors[error])
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        try:
            serializer.create(serializer.validated_data)
            cart.confirmed = True
            cart.save()
            result.set_message("checkout", code="success")
            return Response(result.result, status.HTTP_200_OK)
        except:
            result.set_error("checkout", code="error")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
    