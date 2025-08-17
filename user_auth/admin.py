from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomAdmin(UserAdmin):
    model=CustomUser
    list_display=['username','email','bio']



admin.site.register(CustomUser,CustomAdmin)