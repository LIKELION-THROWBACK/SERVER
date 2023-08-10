from django.db import models
from django.contrib.auth.models import User
from travels.models import Travel

class Review(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='reviews/', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
