from django.urls import path
from buddy.views import BuddyView

urlpatterns = [
    path("", BuddyView.as_view()),
]
