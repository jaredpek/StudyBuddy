from rest_framework import serializers
from django.contrib.auth.models import User
from profiles.models import Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    '''
    A serializer responsible for generating a JSON response for a user's profile details.
    '''
    class Meta:
        model = Profile
        fields = ['mobile_number']
        
class UserRegisterSerializer(serializers.Serializer):
    '''
    A serializer responsible for validating a JSON body for registering a new user in the application.
    '''
    username = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    mobile_number = serializers.CharField()
    
    def validate_email(self, value):
        '''
        Function that validates that the email does not exist
        '''
        user = User.objects.filter(email=value)
        if len(user):
            raise serializers.ValidationError('User with this email already exists.')
    
    def validate_first_name(self, value):
        '''
        Function that validates that the first name only contains alphabets
        '''
        if not value.isalpha():
            raise serializers.ValidationError('This field can only contain letters.')
    
    def validate_last_name(self, value):
        '''
        Function that validates that the last name only contains alphabets
        '''
        if not value.isalpha():
            raise serializers.ValidationError('This field can only contain letters.')

class UserSerializer(serializers.ModelSerializer):
    '''
    Function that generates a JSON response from a user's data.
    '''
    mobile_number = serializers.CharField(source='profile.mobile_number', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'mobile_number', 'date_joined']
        read_only_fields = ['id', 'username', 'date_joined']
