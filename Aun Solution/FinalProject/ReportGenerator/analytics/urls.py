from django.urls import path

from .views import AggrigationView, StatsView, TimeBaseAnalytics

urlpatterns = [
    path("aggrigation/", AggrigationView.as_view(), name="agrigation"),
    path("stats/", StatsView.as_view(), name="stats"),
    path("growth/", TimeBaseAnalytics.as_view(), name="growth"),
]
