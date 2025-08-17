from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from .models import  CustomUser
# Create your views here.
def register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST,request.FILES)
        print(request.FILES)

        if form.is_valid():
            form.save()
            return  redirect('login')
             
        
        else:
            error=form.errors
            return render(request,'register.html',{'form':form,"error":error})
    
    form=RegisterForm()
    return render(request,'register.html',{'form':form})



def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)

        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            user=authenticate(request,username=username,password=password)

            if user:
                login(request,user)
                return redirect('home')
                
        else:
            return render(request,'login.html',{'form':form})
    
    form=AuthenticationForm()
    return render(request,'login.html',{'form':form})



def logout_view(request):
    logout(request)
    return redirect('home')