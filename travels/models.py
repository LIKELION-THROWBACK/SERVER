from django.db import models
from users.models import User

# Create your models here.
class Travel(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    members = models.ManyToManyField(User, related_name="members")
    max_participation = models.IntegerField(null=True, blank=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'host')
    description = models.TextField(blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name