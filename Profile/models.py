from django.db import models
from  django.contrib.auth.models import User
# Create your models here.
from django.conf import settings


class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='p_photos/',null=True,blank=True)
    bio=models.TextField(blank=True,null=True)
    address=models.CharField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.username}"