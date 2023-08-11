from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'travel', 'user', 'title', 'image', 'description', 'created_at')
