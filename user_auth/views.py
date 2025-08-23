from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .forms import NameForm, EmailForm, PhoneForm, PasswordForm,  ProfilePitureForm, BioForm
from django.contrib.auth.forms import AuthenticationForm
User = get_user_model()
def register_view(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        step = request.POST.get('step')
        response = {}

        if step == '1':
            form = NameForm({'username': request.POST.get('name')})
        elif step == '2':
            form = EmailForm({'email': request.POST.get('email')})
        elif step == '3':
            form = PhoneForm({'phone': request.POST.get('phone')})
        elif step == '4':
            form = PasswordForm({'password': request.POST.get('password')})
        elif step == '5':
            form =  ProfilePitureForm(request.POST, request.FILES)
        elif step == '6':
            form = BioForm({'bio': request.POST.get('bio')})
        else:
            response['success'] = False
            response['errors'] = {'step': 'Invalid step'}
            return JsonResponse(response)

        if form.is_valid():
            # Save data in session
            for key, val in form.cleaned_data.items():
                if step!=5:
                   request.session[key] = val
            response['success'] = True


            if step=='6':
                username = request.session.get('username')
                email = request.session.get('email')
                phone_number = request.session.get('phone')
                password = request.session.get('password')
                bio = request.session.get('bio')
                profile_pic=request.FILES.get('profile_piture')
                
                
                



                if User.objects.filter(username=username).exists():
                  return JsonResponse({'success': False, 'errors': {'username': 'Username already exists.'}})
                if User.objects.filter(email=email).exists():
                  return JsonResponse({'success': False, 'errors': {'email': 'Email already registered.'}})


             

                user=User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    phone_number=phone_number,
                    bio=bio

                )

                if profile_pic:
                   user.profile_picture = profile_pic
                   user.save()


                
                
                
                
                response['message'] = "User registered successfully!"



                
                                     
        else:
            response['success'] = False
            response['errors'] = form.errors

        return JsonResponse(response)

    return render(request, 'register.html')



def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            user=authenticate(username=username,password=password)

            if user:
                login(request,user)
                return redirect('home')
            
        return render(request,'login.html',{'form':form})
    
    form=AuthenticationForm()
    return render(request,'login.html',{'form':form})




def logout_view(request):
    logout(request)
    return render(request,'layout.html')
    
        
        





    
    
    
    
    

