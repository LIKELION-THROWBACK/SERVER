from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Travel
from .serializers import TravelSerializer

class TravelListView(ListAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [AllowAny]