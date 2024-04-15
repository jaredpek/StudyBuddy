from rest_framework import serializers
from study_areas.models import StudyArea
from bookings.models import Booking
from django.utils import timezone
from django.db.models import Q
import math

class StudyAreaSerializer(serializers.ModelSerializer):
    '''
    The serializer responsible for generating a JSON response for study area data.
    '''
    created_by = serializers.CharField(source="created_by.username", read_only=True)
    distance = serializers.SerializerMethodField(source="get_distance")
    vacancies = serializers.SerializerMethodField(source="get_vacancies")

    def get_distance(self, obj):
        '''
        The function responsible for calculating the straight line distance between a specified location and the location of the study area.
        '''
        if len(self.context) == 0:
            return 0

        lat_rad = obj.geo_lat/57.29577951
        lng_rad = obj.geo_long/57.29577951

        user_lat_rad = float(self.context.get("lat"))/57.29577951
        user_lng_rad = float(self.context.get("lng"))/57.29577951

        distance = 6385.877 * math.acos((math.sin(lat_rad) * math.sin(user_lat_rad)) + math.cos(lat_rad) * math.cos(user_lat_rad) * math.cos(user_lng_rad - lng_rad))

        return round(distance, 3)

    def get_vacancies(self, obj):
        '''
        The function responsible for computing the number of vacancies in the study area.
        '''
        curr = timezone.localtime()
        area, date, start, end = Q(study_area=obj), Q(date=curr.date()), Q(start_time__lte=curr.time()), Q(end_time__gte=curr.time())
        bookings = Booking.objects.filter(area & date & start & end)
        return obj.capacity - len(bookings)

    class Meta:
        model = StudyArea
        fields = "__all__"
        read_only_fields = ["vacancies"]

class ManageStudyAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyArea
        fields = "__all__"
