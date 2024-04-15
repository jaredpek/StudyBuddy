from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

import json

# Create your tests here.
class ProfilesTestCase(TestCase):
    '''
    Test cases for Profile model
    '''
    def setUp(self):
        '''
        The method responsible for setting up the required data for the tests
        '''
        self.client = APIClient()
    
    def user_registration(self, user_data):
        response = self.client.post('/api/user/auth/register/', user_data, format='json')

        return response

    def user_login(self, user_data):
        response = self.client.post('/api/user/auth/login/', user_data, format='json')

        return response

    def test_user_registration(self):
        '''
        Testing the following:
        - User registration
        '''
        # User registration

        user_data = {
            'username': 'test_user',
            'first_name' : 'test',
            'last_name' : 'user',
            'mobile_number' : '+6512345678',
            'email': 'test_user1@email.com',
            'password1': 'password1',
            'password2': 'password1',
        }

        response = self.user_registration(user_data)

        data = response.content.decode('ascii')
        data = json.loads(data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "success")

    def test_same_user_registration(self):
        '''
        Testing the following:
        - Duplicate User registration
        '''
        # Duplicate user registration

        user_data_1 = {
            'username': 'test_user',
            'first_name' : 'test',
            'last_name' : 'user',
            'mobile_number' : '+6512345678',
            'email': 'test_user@email.com',
            'password1': 'password1',
            'password2': 'password1',
        }

        user_data_2 = {
            'username': 'test_user',
            'first_name' : 'test',
            'last_name' : 'user',
            'mobile_number' : '+6512345678',
            'email': 'test_user@email.com',
            'password1': 'password1',
            'password2': 'password1',
        }

        response1 = self.user_registration(user_data_1)
        response2 = self.user_registration(user_data_2)
        
        data1 = response1.content.decode('ascii')
        data1 = json.loads(data1)

        data2 = response2.content.decode('ascii')
        data2 = json.loads(data2)

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(data1["status"], "success")

        self.assertEqual(response2.status_code, 400)
        self.assertEqual(data2["status"], "error")

    def test_user_login(self):
        '''
        Testing the following:
        - Valid Credentials Login
        - Invalid Credentials Login
        '''
        # Valid Credentials Login
        
        user_data = {
            'username': 'test_user',
            'first_name' : 'test',
            'last_name' : 'user',
            'mobile_number' : '+6512345678',
            'email': 'test_user1@email.com',
            'password1': 'password1',
            'password2': 'password1',
        }

        self.user_registration(user_data)

        user_data = {
            'username': 'test_user',
            'password': 'password1'
        }

        response = self.user_login(user_data)

        data = response.content.decode('ascii')
        data = json.loads(data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "success")

        # Invalid Credentials Login

        user_data = {
            'username': 'admins',
            'password': 'password122'
        }

        response = self.user_login(user_data)

        data = response.content.decode('ascii')
        data = json.loads(data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["status"], "error")