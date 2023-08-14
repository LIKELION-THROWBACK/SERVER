from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Review
from users.models import User
from travels.models import Travel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname', 'profile_image') 

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = ('name', 'start_date')
        
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) 
    travel = TravelSerializer(read_only=True) 
    class Meta:
        model = Review
        fields = ('id', 'travel', 'user', 'title', 'image', 'description', 'created_at')

from rest_framework import serializers

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()
