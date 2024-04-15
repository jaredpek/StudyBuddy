from rest_framework import serializers, validators
from bookings.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    '''
    The serializer responsible for generating a JSON response for bookings.
    '''
    study_area_id = serializers.IntegerField(source="study_area.pk", read_only=True)
    study_area = serializers.CharField(source="study_area.name", read_only=True)
    image = serializers.FileField(source="study_area.image", read_only=True)
    user = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = Booking
        fields = "__all__"
        read_only_fields = ["image"]

class ManageBookingSerializer(serializers.ModelSerializer):
    '''
    The serializer responsible for validating a JSON body when creating or updating a booking.
    '''
    class Meta:
        model = Booking
        fields = "__all__"
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Booking.objects.all(),
                fields = ["date", "start_time", "end_time", "user"]
            )
        ]
