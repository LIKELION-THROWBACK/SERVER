from django.urls import path

from .views import TravelListView, TravelDetailView
urlpatterns = [
    path('list/', TravelListView.as_view()),
    path('detail/<str:travel_name>', TravelDetailView.as_view()),
]