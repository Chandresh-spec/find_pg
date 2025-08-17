from django  import  forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):

    class Meta:
        model=CustomUser
        fields=('username','email','phone_number','profile_pic','bio','password1','password2')
        

