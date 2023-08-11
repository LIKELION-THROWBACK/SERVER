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
    host_profile_image = serializers.SerializerMethodField()
    current_member = serializers.SerializerMethodField()
    class Meta:
        model = Travel
        fields = ['name', 'image', 'start_date', 'end_date', 'host', 'host_profile_image', 'current_member', 'max_participation']

    def get_current_member(self, obj):
        return obj.members.count()
    
    def get_host_profile_image(self, obj):
        try:
            return obj.host.profile_image.url
        except ValueError:
            return None


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
    host_profile_image = serializers.SerializerMethodField()
    left_day = serializers.SerializerMethodField()
    current_member = serializers.SerializerMethodField()
    class Meta:
        model = Travel
        fields = '__all__'

    def get_left_day(self, obj):
        return (obj.start_date - date.today()).days
    
    def get_current_member(self, obj):
        return obj.members.count()
    
    def get_host_profile_image(self, obj):
        try:
            return obj.host.profile_image.url
        except ValueError:
            return None