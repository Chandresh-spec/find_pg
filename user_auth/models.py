from django.db import models
# Create your models here.

from django.contrib.auth.models import AbstractUser

from django.db import models

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=10,blank=False,null=False)
    profile_pic=models.ImageField(upload_to='p_photos/',null=True)
    bio=models.CharField(max_length=150,blank=True,null=True)



    def __str__(self):
        return self.username