from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Travel
from .serializers import TravelSerializer

class TravelListView(ListAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [AllowAny]

class TravelDetailView(RetrieveAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = Travel.objects.get(name = kwargs['travel_name'])
        except Travel.DoesNotExist:
            return Response({'message': '해당 여행은 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)