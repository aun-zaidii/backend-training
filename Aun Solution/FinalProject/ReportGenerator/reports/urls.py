from django.urls import path

from .views import *








urlpatterns = [
    path('testreport/' , CensusReportView.as_view(),  name= 'test_report'),
]
