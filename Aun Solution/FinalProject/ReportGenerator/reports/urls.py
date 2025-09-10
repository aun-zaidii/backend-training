from django.urls import path

from .views import CountyReportView, DetailReportView

urlpatterns = [
    path("county_report/", CountyReportView.as_view(), name="county_report"),
    path("detail_report/", DetailReportView.as_view(), name="detail_report"),
]
