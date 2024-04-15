from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from project.response import Response as Result
from products.serializers import ProductSerializer

from products.models import Product

class ProductsView(APIView):
    '''
    The view for products API.
    - GET /api/products/ (User views all available products in the store)
    '''
    queryset = Product.objects.all()
    permission_classes = [AllowAny, ]

    def get(self, request):
        '''
        The function responsible for retrieving all available products in the store.
        '''
        queryItem = request.GET.get("instock")
        result = Result()
        products = ProductSerializer(self.queryset.filter(), many=True).data

        if queryItem is not None:
            products = ProductSerializer(self.queryset.filter(stock__gt=0), many=True).data
        
        result.set_message("products", products, as_list=False)
        result.set_message("count", len(products), as_list=False)
        return Response(result.result, status.HTTP_200_OK)

class ProductView(APIView):
    '''
    The view for product API.
    - GET /api/products/<int:pk>/ (User views all a specific product in the store)
    '''
    queryset = Product.objects.all()
    permission_classes = [AllowAny, ]

    def get(self, request, pk):
        '''
        The function responsible for retrieving a specific product in the store.
        '''
        result = Result()
        try:
            study_area = Product.objects.get(pk=pk)
            result.result.update(ProductSerializer(study_area).data)
            return Response(result.result, status.HTTP_200_OK)
        except Exception:
            result.set_error("product", code="does_not_exist")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)