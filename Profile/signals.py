from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile
from django.db.models.signals import post_save
User = get_user_model()

@receiver(post_save,sender=User)

def create_profile(sender,instance,created,**kwargs):
    if created:
        user=Profile.objects.create(user=instance)
        user.save()
