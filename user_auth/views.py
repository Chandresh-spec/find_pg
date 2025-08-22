from django.shortcuts import render
from django.http import JsonResponse
from .forms import NameForm, EmailForm, PhoneForm, PasswordForm,  ProfilePitureForm, BioForm

def step_form(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        step = request.POST.get('step')
        response = {}

        if step == '1':
            form = NameForm({'name': request.POST.get('name')})
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
                request.session[key] = val
            response['success'] = True
        else:
            response['success'] = False
            response['errors'] = form.errors

        return JsonResponse(response)

    return render(request, 'register.html')
