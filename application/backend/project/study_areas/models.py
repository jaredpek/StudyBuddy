from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator

import os
import googlemaps

gmaps = googlemaps.Client(key=os.getenv("GMAP_SECRET"))

class StudyArea(models.Model):
    '''
    The study area model that contains all the relevant information pertaining to a study area.
    '''
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, unique=True)

    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=6, validators=[RegexValidator("^\d{6}$")])
    block = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    level = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    unit_number = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    capacity = models.IntegerField(validators=[MinValueValidator(10)])
    open_time = models.TimeField()
    close_time = models.TimeField()
    image = models.ImageField(upload_to="images/")
    geo_lat = models.FloatField(blank=True, null=True)
    geo_long = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} | {self.capacity} | {self.open_time}-{self.close_time} | {self.address} #{self.level}-{self.unit_number}, {self.postal_code}"
    
    # Overriding save method to compute lat and lng when a new object is added to study area
    def save(self, *args, **kwargs):
        '''
        Function responsible for saving new attribute values for study area objects, and saving its latitude and longitude.
        '''
        self.get_latlong()
        super(StudyArea, self).save(*args, **kwargs)

    def get_latlong(self):
        '''
        Function responsible for retrieving the study area's latitude and longitude via Google Maps API.
        '''
        data = {"lat" : 0, "lng" : 0}

        try:
            data = gmaps.geocode(f"{self.address} {self.postal_code}")[0]
            data = data["geometry"]["location"]
        except:
            data = {"lat" : 0, "lng" : 0}

        self.geo_lat = data["lat"]
        self.geo_long = data["lng"]
    