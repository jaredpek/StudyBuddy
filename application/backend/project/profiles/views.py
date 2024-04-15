from datetime import datetime, timedelta
from project.settings import LIFETIME
from django.contrib.auth.models import User
from project.response import Response as Result
from profiles.serializers import UserSerializer, ProfileSerializer, UserRegisterSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from dj_rest_auth.views import LoginView, LogoutView as BaseLogoutView
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.registration.serializers import RegisterSerializer

def convertDate(date):
    '''
    Function responsible for converting a date into a milisecond-based timestamp.
    '''
    return int(date.timestamp() * 1000)

def getLifetime(lifetime=LIFETIME):
    '''
    Function responsible for generating the creation and expiry times of a JWT token.
    '''
    today = datetime.now()
    expiry = today + timedelta(days=lifetime)
    return {
        'created': convertDate(today),
        'expires': convertDate(expiry)
    } 

class CredentialLoginView(LoginView):
    '''
    The view for login API.
    - POST /api/users/auth/login/ (User logs in to the application)
    '''
    def post(self, request, *args, **kwargs):
        '''
        The function responsible for authenticating a user to the application.
        '''
        result = Result()
        
        try:
            data = super().post(request, *args, **kwargs).data
            result.set_message('login', code='success')
            result.result.update({
                'access': data.get('access'),
                'refresh': data.get('refresh'),
            })
            result.result.update(getLifetime())
            return Response(result.result, status.HTTP_200_OK)
        except Exception:
            result.set_error('login', error='Invalid "username" or "password" provided.')
            return Response(result.result, status.HTTP_400_BAD_REQUEST)

class CredentialRegisterView(RegisterView):
    '''
    The view for register API.
    - POST /api/users/auth/register/ (User registers an account in the application)
    '''
    def post(self, request, *args, **kwargs):
        '''
        The function responsible for creating a new account and authenticating the user to the application.
        '''
        result = Result()
        initial_register_serializer = UserRegisterSerializer(data=request.data)
        register_serializer = RegisterSerializer(data=request.data)
        user_serializer = UserSerializer(data=request.data)
        profile_serializer = ProfileSerializer(data=request.data)
        
        for serializer in [initial_register_serializer, register_serializer, user_serializer, profile_serializer]:
            if not serializer.is_valid():
                errors = serializer.errors
                for field in errors:
                    result.set_errors(field, errors[field], replace=True)
        if result.result["status"] == "error":
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        
        try:
            data = super().post(request).data
            user = User.objects.get(pk=data["user"]["pk"])
            for serializer in [UserSerializer(user, request.data), ProfileSerializer(user.profile, request.data)]:
                serializer.is_valid()
                serializer.save()
            result.set_message('access', data['access'], as_list=False)
            result.set_message('registration', code='success')
            return Response(result.result, status.HTTP_200_OK)
        except Exception:
            result.set_error('registration', code='error')
            return Response(result.result, status.HTTP_400_BAD_REQUEST)

class LogoutView(BaseLogoutView):
    '''
    The view for logout API.
    - POST /api/users/auth/logout/ (User logs out from the application, old refresh token is blacklisted)
    '''
    def post(self, request, *args, **kwargs):
        '''
        The function responsible for logging the user out and blacklisting the old refresh token.
        '''
        result = Result()
        message = super().post(request, *args, **kwargs).data.get('detail')
        if 'success' in message.lower():
            result.set_message('logout', code='success')
            return Response(result.result, status.HTTP_200_OK)
        result.set_error('logout', error='User is already logged out.')
        return Response(result.result, status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    '''
    The view for profile API.
    - POST /api/users/profile/ (User logs out from the application, old refresh token is blacklisted)
    '''
    queryset = User.objects.all()
    
    def get(self, request):
        '''
        The function responsible for getting the profile details for a user.
        '''
        result = Result()
        try:
            user = self.queryset.get(id=request.user.id)
            result.result.update(UserSerializer(user).data)
            return Response(result.result, status.HTTP_200_OK)
        except Exception:
            result.set_error('user', code='does_not_exist')
            return Response(result.result, status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        '''
        The function responsible for updating a user's profile details.
        '''
        result = Result()
        user_serializer = UserSerializer(request.user, request.data)
        profile_serializer = ProfileSerializer(request.user.profile, request.data)

        if not user_serializer.is_valid() or not profile_serializer.is_valid():
            for serializer in [user_serializer, profile_serializer]:
                errors = serializer.errors
                for field in errors:
                    result.set_errors(field, errors[field])
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        
        user_serializer.save()
        profile_serializer.save()
        result.set_message('update', code='success')
        return Response(result.result, status.HTTP_200_OK)
