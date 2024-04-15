from datetime import datetime, timedelta
from django.utils import timezone

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from project.response import Response as Result
from bookings.serializers import BookingSerializer, ManageBookingSerializer
from bookings.models import Booking

def str_to_datetime(string):
    '''
    Converts a date in string format into a date in datetime format.
    '''
    return datetime.strptime(string, "%H:%M:%S")

def valid_present_time(date, start, end, result):
    '''
    Verifies that the provided start and end times are valid.
    A time slot is invalid if:
    - date < current date OR
    - date == current date AND start and end times < current time
    '''
    curr = timezone.localtime()
    curr_date, curr_time = curr.date(), curr.time()
    if date < curr_date or (date == curr_date and start < curr_time and end < curr_time):
        result.set_error("time_slot", "Time slot cannot be in the past")
    return True if result.result["status"] == "success" else False

def valid_time_entries(start, end, result):
    '''
    Verifies that start and end times are valid.
    Timings are valid if:
    - Time starts at the start of the hour (minutes and seconds = 0) AND
    - Time interval between start and end times = 1 hour
    '''
    start, end = str_to_datetime(f"{start}"), str_to_datetime(f"{end}")
    message = "Time slots are in multiples of 1 hour (e.g. 10:30 is not allowed, 10:00 is allowed)"
    if start.minute != 0:
        result.set_error("start_time", message)
    if end.minute != 0:
        result.set_error("end_time", message)
    if (end - start) != timedelta(hours=1):
        result.set_error("time_slot", "Each time slot must be in 1 hour time intervals")
    return True if result.result["status"] == "success" else False

def valid_time_operating(slot_start, slot_end, area_open, area_close, result):
    '''
    Verifies that the time slot occurs during the study area's operating hours.
    '''
    slot_start, slot_end = str_to_datetime(f"{slot_start}"), str_to_datetime(f"{slot_end}")
    area_open, area_close = str_to_datetime(f"{area_open}"), str_to_datetime(f"{area_close}")
    if slot_start < area_open or area_close < slot_end:
        result.set_error("time_slot", "This time slot is outside of operating hours.")
        return False
    return True

def sufficient_capacity(study_area, start_time, end_time, result):
    '''
    Verifies that the study area has sufficient capacity at the specified booking time slot.
    '''
    booked_slots = Booking.objects.filter(study_area=study_area, start_time=start_time, end_time=end_time)
    if len(booked_slots) >= study_area.capacity:
        result.set_error("capacity", "No available slots at this time.")
        return False
    return True

class BookingsView(APIView):
    '''
    The view for bookings-related APIs.
    - GET /api/bookings/ (Retrieve a user's bookings)
    - POST /api/bookings/ (User creates a new booking)
    '''
    permission_classes = [IsAuthenticated, ]
    queryset = Booking.objects.all()
    
    def get(self, request):
        '''
        The function that handles the retrieval of a user's bookings.
        '''
        result = Result()
        bookings = BookingSerializer(self.queryset.filter(user=request.user).order_by('-date', '-start_time'), many=True).data
        
        result.set_message("bookings", bookings, as_list=False)
        result.set_message("count", len(bookings), as_list=False)
        return Response(result.result, status.HTTP_200_OK)
    
    def post(self, request):
        '''
        The function that handles the creation of a new booking for a user.
        '''
        result = Result()
        request.data.update({"user": request.user.pk})
        serializer = ManageBookingSerializer(data=request.data)
        if not serializer.is_valid():
            for error in serializer.errors:
                result.set_errors(error, serializer.errors[error])
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        if not valid_present_time(serializer.validated_data["date"], serializer.validated_data["start_time"], serializer.validated_data["end_time"], result):
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        if not valid_time_entries(serializer.validated_data["start_time"], serializer.validated_data["end_time"], result):
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        study_area = serializer.validated_data["study_area"]
        if not valid_time_operating(serializer.validated_data["start_time"], serializer.validated_data["end_time"], study_area.open_time, study_area.close_time, result):
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        if not sufficient_capacity(study_area, serializer.validated_data["start_time"], serializer.validated_data["end_time"], result):
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        try:
            serializer.create(serializer.validated_data)
            result.set_message("create", code="success")
            return Response(result.result, status.HTTP_201_CREATED)
        except Exception:
            result.set_error("create", code="error")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        
class BookingView(APIView):
    '''
    The view for specific booking-related APIs.
    - GET /api/bookings/<int:pk>/ (Retrieve a user's booking)
    - PUT /api/bookings/<int:pk>/ (User updates a specific booking)
    - DELETE /api/bookings/<int:pk>/ (User deletes a specific booking)
    '''
    permission_classes = [IsAuthenticated, ]
    queryset = Booking.objects.all()
    
    def get(self, request, pk):
        '''
        The function that handles the retrieval of a specific booking.
        '''
        result = Result()
        try:
            booking = self.queryset.get(user=request.user, pk=pk)
            result.result.update(BookingSerializer(booking).data)
            return Response(result.result, status.HTTP_200_OK)
        except:
            result.set_error("booking", code="does_not_exist")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        '''
        The function that handles the updating of a specific booking.
        '''
        result = Result()
        request.data.update({"user": request.user.pk})
        try:
            booking = Booking.objects.get(user=request.user, pk=pk)
            request.data.update({"study_area": booking.study_area.pk})
        except:
            result.set_error("booking", code="does_not_exist")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        serializer = ManageBookingSerializer(booking, data=request.data)
        if not serializer.is_valid():
            for error in serializer.errors:
                result.set_errors(error, serializer.errors[error])
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        if not valid_time_entries(serializer.validated_data["start_time"], serializer.validated_data["end_time"], result):
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        study_area = serializer.validated_data["study_area"]
        if not valid_present_time(serializer.validated_data["date"], serializer.validated_data["start_time"], serializer.validated_data["end_time"], result):
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        if not valid_time_operating(serializer.validated_data["start_time"], serializer.validated_data["end_time"], study_area.open_time, study_area.close_time, result):
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        if not sufficient_capacity(study_area, serializer.validated_data["start_time"], serializer.validated_data["end_time"], result):
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        try:
            serializer.save()
            result.set_message("update", code="success")
            return Response(result.result, status.HTTP_201_CREATED)
        except Exception:
            result.set_error("update", code="error")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        '''
        The function that handles the deletion of a specific booking.
        '''
        result = Result()
        try:
            booking = Booking.objects.get(user=request.user, pk=pk)
            booking.delete()
            result.set_message("delete", code="success")
            return Response(result.result, status.HTTP_200_OK)
        except:
            result.set_error("booking", code="does_not_exist")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        