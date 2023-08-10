from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer
from django.shortcuts import render

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

