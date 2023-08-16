from django.db import models

# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='users/', null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name