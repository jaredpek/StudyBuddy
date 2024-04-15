from django.urls import path
from bookings.views import BookingsView, BookingView

urlpatterns = [
    path("", BookingsView.as_view()),
    path("<int:pk>/", BookingView.as_view()),
]
