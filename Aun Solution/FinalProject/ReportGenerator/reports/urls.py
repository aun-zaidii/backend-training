from django.urls import path

from .views import (CountyReportCsvView, CountyReportJsonView,
                    DetailReportCsvView, DetailReportJsonView)

urlpatterns = [
    path("county_report/csv/", CountyReportCsvView.as_view(), name="county_report_csv"),
    path(
        "county_report/json/", CountyReportJsonView.as_view(), name="county_report_json"
    ),
    path("detail_report/csv/", DetailReportCsvView.as_view(), name="detail_report_csv"),
    path(
        "detail_report/json/", DetailReportJsonView.as_view(), name="detail_report_json"
    ),
]
