from django.urls import path
from orders.views import OrdersView, OrderView

urlpatterns = [
    path("", OrdersView.as_view()),
    path("<int:pk>/", OrderView.as_view()),
]
