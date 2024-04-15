from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from project.response import Response as Result
from orders.models import Order
from orders.serializers import OrderSerializer

class OrdersView(APIView):
    '''
    The view for orders API.
    - GET /api/orders/ (User views all his past and current orders)
    '''
    queryset = Order.objects.all()
    
    def get(self, request):
        '''
        The function responsible for retrieving all the user's orders.
        '''
        result = Result()
        orders = OrderSerializer(self.queryset.filter(user=request.user).order_by("-date_ordered"), many=True).data
        for order in orders:
            order["items"] = order["cart"]["items"]
            for item in order["items"]:
                item["subtotal"] = item["price"] * item["quantity"]
            order.pop("cart")
        result.set_messages("orders", orders)
        return Response(result.result, status.HTTP_200_OK)
    
class OrderView(APIView):
    '''
    The view for order API.
    - GET /api/orders/<int:pk>/ (User views a specific order that he made)
    '''
    queryset = Order.objects.all()
    
    def get(self, request, pk):
        '''
        The function responsible for retrieving a specific order for a user.
        '''
        result = Result()
        try:
            order = OrderSerializer(self.queryset.get(user=request.user, pk=pk)).data
            result.result.update(order)
            return Response(result.result, status.HTTP_200_OK)
        except:
            result.set_error("order", code="does_not_exist")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
    