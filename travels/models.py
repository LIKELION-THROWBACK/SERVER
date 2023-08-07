from django.db import models
from users.models import User

# Create your models here.
class Travel(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    deadline = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name="participants")
    max_participation = models.IntegerField(null=True, blank=True)
    host_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'host')
    description = models.TextField(blank=True)
    price = models.IntegerField(null=True, blank=True)
    