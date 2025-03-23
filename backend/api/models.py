from django.db import models
from django.contrib.auth import User

class Profile(models.Models):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(primary_key=True, default=0)
    bio = models.TextField(blank=True, default='')
    profile_img = models.ImageField(upload_to='profile_images', default=None)
    
    def __str__(self):
        return self.user.username
    
