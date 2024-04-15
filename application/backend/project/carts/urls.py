from django.urls import path
from carts.views import CartView, CheckOutView

urlpatterns = [
    path("", CartView.as_view()),
    path("checkout/", CheckOutView.as_view()),
]
