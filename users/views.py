from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from datetime import date
from .models import User
from travels.models import Travel
from reviews.models import Review
from .serializers import UserSerializer 
from travels.serializers import TravelListSerializer
from reviews.serializers import ReviewSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['GET'])
    def upcoming_travels_count(self, request, *args, **kwargs):
        user = self.get_object()
        today = date.today()
        upcoming_travels_count = Travel.objects.filter(members=user, start_date__gt=today).count()
        return Response({'upcoming_travels_count': upcoming_travels_count})

    @action(detail=True, methods=['GET'])
    def finished_travels_count(self, request, *args, **kwargs):
        user = self.get_object()
        today = date.today()
        finished_travels_count = Travel.objects.filter(members=user, end_date__lt=today).count()
        return Response({'finished_travels_count': finished_travels_count})

    @action(detail=True, methods=['GET'])
    def my_reviews(self, request, *args, **kwargs):
        user = self.get_object()
        reviews = Review.objects.filter(user=user)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)