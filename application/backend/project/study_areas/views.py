from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from project.response import Response as Result
from study_areas.models import StudyArea
from study_areas.serializers import StudyAreaSerializer, ManageStudyAreaSerializer

class StudyAreasView(APIView):
    '''
    The view for study areas API.
    - GET /api/study_areas/ (User views all available study areas)
    '''
    queryset = StudyArea.objects.all()
    permission_classes = [AllowAny, ]
    
    def get(self, request):
        '''
        The function responsible for retrieving all available study areas.
        Includes queries lat & lng
        lat : latitude of user (float)
        lng : longitude of user (float)
        Returns distance of study areas to user field from given coordinates
        - GET /api/study_areas?lat=<float>&lng=<float>
        '''
        result = Result()
        context = {"lat": request.GET.get("lat"), "lng": request.GET.get("lng")}
        if context["lat"] and context["lng"]:
            study_areas = sorted(
                StudyAreaSerializer(self.queryset.filter(), many=True, context=context).data,
                key=lambda x: x['distance']
            ) 
        else:
            study_areas = sorted(
                StudyAreaSerializer(self.queryset.filter(), many=True).data,
                key=lambda x: x['name']
            )
        result.set_message("study_areas", study_areas, as_list=False)
        result.set_message("count", len(study_areas), as_list=False)
        return Response(result.result, status.HTTP_200_OK)

class StudyAreaView(APIView):
    '''
    The view for study area API.
    - GET /api/study_area/<int:pk>/ (User views a specific study area)
    '''
    queryset = StudyArea.objects.all()
    permission_classes = [AllowAny, ]
    
    def get(self, request, pk):
        '''
        The function responsible for retrieving a specific study area.
        Includes queries lat & lng
        lat : latitude of user (float)
        lng : longitude of user (float)
        Returns distance of study area to user field from given coordinates
        - GET /api/study_area/<int:pk>?lat=<float>&lng=<float>
        '''
        result = Result()

        try:
            study_area = StudyArea.objects.get(pk=pk)
            
            user_lat = request.GET.get("lat")
            user_lng = request.GET.get("lng")

            if user_lat is not None and user_lng is not None:
                study_area = StudyAreaSerializer(study_area, context={"lat" : user_lat, "lng" : user_lng}).data
            else:
                 study_area = StudyAreaSerializer(study_area).data

            result.result.update(study_area)
            return Response(result.result, status.HTTP_200_OK)
        except Exception:
            result.set_error("study_area", code="does_not_exist")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        