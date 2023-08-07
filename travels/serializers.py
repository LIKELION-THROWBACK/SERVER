from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Travel
from users.models import User

class TravelSerializer(ModelSerializer):
    member = serializers.SlugRelatedField(
        many=True,
        queryset=User.objects.all(),
        slug_field='name'
    )
    host = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = Travel
        fields = '__all__'