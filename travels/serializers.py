from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from datetime import date

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
        return obj.members.count()


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
    left_day = serializers.SerializerMethodField()
    current_member = serializers.SerializerMethodField()
    class Meta:
        model = Travel
        fields = '__all__'

    def get_left_day(request, obj):
        return (obj.deadline - date.today()).days
    
    def get_current_member(request, obj):
        return obj.members.count()