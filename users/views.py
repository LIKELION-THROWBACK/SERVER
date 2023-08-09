from rest_framework.viewsets import ModelViewSet

from .models import  User

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    