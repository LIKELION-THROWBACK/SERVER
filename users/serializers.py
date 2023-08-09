from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from datetime import date
from urllib.parse import quote

from .models import User

class UserSerializer(ModelSerializer):
  class Meta :
    model = User
    fields = '__all__'