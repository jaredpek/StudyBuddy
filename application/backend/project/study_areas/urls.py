from django.urls import path
from study_areas.views import StudyAreasView, StudyAreaView

urlpatterns = [
    path("", StudyAreasView.as_view()),
    path("<int:pk>/", StudyAreaView.as_view())
]
