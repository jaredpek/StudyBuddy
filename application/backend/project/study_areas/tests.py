from django.test import TestCase
from study_areas.models import StudyArea
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime
import json

class StudyAreaTestCase(TestCase):
    '''
    Test cases for StudyArea model
    '''
    def setUp(self):
        '''
        The method responsible for setting up the required data for the tests
        '''
        user_test = User.objects.create_superuser(username="tester", email="test@gmail.com", password="123")

        case1 = {
            'created_by' : user_test,
            'name' : 'Study Area 1',
            'address' : '66 Nanyang Crescent',
            'postal_code' : 636960,
            'capacity' : 20,
            'open_time' : datetime.time(6, 30, 0),
            'close_time' : datetime.time(18, 30, 0),
            'image' : SimpleUploadedFile("face.jpg", b"")
        }

        self.study_area = StudyArea.objects.create(**case1)
        self.client = APIClient()

    def test_distance_check(self):
        '''
        Testing the following:
        - Distance field calculation from given coordinates
        '''
        
        response = self.client.get('/api/study_areas/1/', QUERY_STRING=f'lat={self.study_area.geo_lat}&lng={self.study_area.geo_long}')
        data = response.content.decode('ascii')
        data = json.loads(data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['distance'], 0.0)

# Create your tests here.
