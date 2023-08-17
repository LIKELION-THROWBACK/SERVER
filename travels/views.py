from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action

from datetime import date
from .models import Travel, User
from .serializers import TravelDetailSerializer, TravelListSerializer

from django.db.models import F, Count
    
class TravelViewSet(ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = Travel.objects.get(id = kwargs['id'])
        except Travel.DoesNotExist:
            return Response({'message': '해당 여행은 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).annotate(
            members_count=Count('members')).filter(
            max_participation__gt=F('members_count')).filter(
            start_date__gt=str(date.today())).order_by('-id')

        serializer = TravelListSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def add_user(self, request, name=None):
        user_id = request.data.get('id')
        user = User.objects.get(id=user_id)
        travel = Travel.objects.get(name=name)
        if travel.members.count() < travel.max_participation:
            travel.members.add(user)
            return Response({'message': f'{user.name}님의 참가 신청이 완료되었습니다.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': '모집이 완료된 여행입니다.'}, status=status.HTTP_400_BAD_REQUEST)