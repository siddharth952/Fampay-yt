from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publishTime = models.DateTimeField(default=timezone.now)
    thumbnail_url = models.URLField
    channelTitle = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title