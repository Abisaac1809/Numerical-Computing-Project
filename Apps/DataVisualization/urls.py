from django.urls import path

from Apps.DataVisualization.views import generateRandomGraphAndPoints

urlpatterns = [
    path("getRandomGraphAndPoints/", generateRandomGraphAndPoints, name="getRandomGraphAndPoints"),
]
