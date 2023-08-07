from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter

from .models import Travel
from .serializers import TravelSerializer
    
class TravelViewSet(ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [AllowAny]
    lookup_field = 'name'
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = Travel.objects.get(name = kwargs['name'])
        except Travel.DoesNotExist:
            return Response({'message': '해당 여행은 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).order_by('-id')

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)