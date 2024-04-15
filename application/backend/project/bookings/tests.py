from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from django.contrib.auth.models import User
from study_areas.models import StudyArea
from rest_framework.test import APIClient

import datetime
import json

# Create your tests here.
class BookingTestCase(TestCase):
    '''
    Test cases for Booking model
    '''
    def setUp(self):
        '''
        The method responsible for setting up the required data for the tests
        '''
        self.client = APIClient()
        self.user_test = User.objects.create_user(username="tester", email="test@gmail.com", password="123")
        self.user_super = User.objects.create_superuser(username="tester_super", email="tester_super@gmail.com", password="123")

        study_data = {
            'created_by' : self.user_super,
            'name' : 'Study Area 1',
            'address' : '66 Nanyang Crescent',
            'postal_code' : 636960,
            'capacity' : 20,
            'open_time' : datetime.time(6, 30, 0),
            'close_time' : datetime.time(18, 30, 0),
            'image' : SimpleUploadedFile("face.jpg", b"")
        }

        self.study_area = StudyArea.objects.create(**study_data)

        user = User.objects.get(username="tester")

        self.client.login(username="tester", password="123")
        self.client.force_authenticate(user=user)

    def book_studyarea(self, data):
        response = self.client.post('/api/bookings/', data, format='json')

        return response

    def view_booking(self, pk):
        response = self.client.get(f'/api/bookings/{pk}/')

        return response

    def delete_booking(self, pk):
        response = self.client.delete(f'/api/bookings/{pk}/')

        return response

    def test_booking(self):
        '''
        Testing the following:
        - Booking study area with valid data
        - Booking study area with invalid data
        - View booking of study area
        - Delete booking of study area
        '''
        user_response = self.client.get('/api/user/profile/')

        user_data = user_response.content.decode('ascii')
        user_data = json.loads(user_data)

        # Create Booking

        data = {
            'date' : datetime.date(2024, 4, 7),
            'start_time' : datetime.time(12,0,0),
            'end_time' : datetime.time(13,0,0),
            'study_area' : 1,
            'user' : user_data
        }

        booking_response = self.book_studyarea(data)
        booking_data = booking_response.content.decode('ascii')
        booking_data = json.loads(booking_data)

        self.assertEqual(booking_response.status_code, 201)
        self.assertEqual(booking_data["status"], "success")

        # Create invalid booking
        
        invalid_data = {
            'date' : datetime.date(2024, 4, 7),
            'start_time' : datetime.time(5,0,0),
            'end_time' : datetime.time(6,0,0),
            'study_area' : 1,
            'user' : user_data
        }

        invalid_response = self.book_studyarea(invalid_data)
        invalid_data = invalid_response.content.decode('ascii')
        invalid_data = json.loads(invalid_data)

        self.assertEqual(invalid_response.status_code, 400)
        self.assertEqual(invalid_data["status"], "error")

        # View Booking

        view_response = self.view_booking(1)
        view_data = view_response.content.decode('ascii')
        view_data = json.loads(view_data)
        
        self.assertEqual(view_response.status_code, 200)
        self.assertEqual(view_data["status"], "success")

        # Delete Booking

        delete_response = self.delete_booking(1)
        delete_data = delete_response.content.decode('ascii')
        delete_data = json.loads(delete_data)

        self.assertEqual(view_response.status_code, 200)
        self.assertEqual(view_data["status"], "success")