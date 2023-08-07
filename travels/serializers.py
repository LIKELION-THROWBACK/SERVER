from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Travel
from users.models import User

class TravelListSerializer(ModelSerializer):
    host = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='name'
    )
    current_member = serializers.SerializerMethodField()
    class Meta:
        model = Travel
        fields = ['name', 'image', 'start_date', 'end_date', 'host', 'current_member', 'max_participation']

    def get_current_member(request, obj):
        return obj.get_current_member()


class TravelDetailSerializer(ModelSerializer):
    members = serializers.SlugRelatedField(
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