from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from datetime import date

from .models import User
from reviews.models import Review
from travels.models import Travel

class UserSerializer(ModelSerializer):
    my_reviews = serializers.SerializerMethodField()
    upcoming_travels_count = serializers.SerializerMethodField()
    finished_travels_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_upcoming_travels_count(self, obj):
        today = date.today()
        return Travel.objects.filter(members=obj, start_date__gte=today).count()

    def get_finished_travels_count(self, obj):
        today = date.today()
        return Travel.objects.filter(members=obj, end_date__lt=today).count()

    def get_my_reviews(self, obj):
        return Review.objects.filter(user=obj).values('title', 'image', 'description', 'created_at')
    

from rest_framework import serializers

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()
