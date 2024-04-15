from django.db import models
from study_areas.models import StudyArea
from django.contrib.auth.models import User

class Booking(models.Model):
    '''
    The booking model with relevant fields to capture crucial information for users' bookings.
    '''
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    study_area = models.ForeignKey(StudyArea, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} | {self.study_area.name} | {self.date} | {self.start_time}-{self.end_time}"
