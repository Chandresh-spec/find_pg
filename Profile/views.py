from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import EditForm
# Create your views here.

@login_required
def profile_view(request):

    profile=get_object_or_404(Profile,user=request.user)
    return render(request,'profile.html',{'profile':profile})



@login_required
def profile_edit_view(request):
    profile=request.user.profile
    if request.method=='POST':
        form=EditForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
        return render(request,'profile_edit_page.html',{'form':form})
    
    form = EditForm(instance=profile)
    return render(request,'profile_edit_page.html',{'form':form})


    