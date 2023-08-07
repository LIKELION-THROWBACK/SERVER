from django.urls import path

from .views import TravelListView
urlpatterns = [
    path('list/', TravelListView.as_view()),
]