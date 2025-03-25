from datetime import datetime
import uuid
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(primary_key=True, default=0)
    bio = models.TextField(blank=True, default='')
    profile_img = models.ImageField(upload_to='profile_images', default=None)
    location = models.CharField(max_length=100, blank=True, default='')
    
    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    id_post = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images/')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    num_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user