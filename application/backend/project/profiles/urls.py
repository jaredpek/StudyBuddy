from django.urls import path
from dj_rest_auth.jwt_auth import get_refresh_view
from profiles.views import CredentialLoginView, CredentialRegisterView, LogoutView, ProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view()),
    path('auth/login/', CredentialLoginView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    path('auth/refresh/', get_refresh_view().as_view()),
    path('auth/register/', CredentialRegisterView.as_view()),
]
