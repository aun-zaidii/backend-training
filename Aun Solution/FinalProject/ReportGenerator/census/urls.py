from django.urls import path

from .views import DataFetchView, ManualFetchView, StatusLog

urlpatterns = [
    path("fetch/", DataFetchView.as_view(), name="data_fetch"),
    path("statuslog/", StatusLog.as_view(), name="status_log"),
    path("testsave/", ManualFetchView.as_view(), name="manual_fetch"),
]
