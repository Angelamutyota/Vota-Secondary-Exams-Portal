from votapp.forms import PersonalinfoForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):

    return render(request,'index.html')

@login_required(login_url='/accounts/login/')    
def personal_info(request):
    if request.method == 'POST':
        profile_form = PersonalinfoForm(request.POST, request.FILES, instance=request.user)
        if  profile_form.is_valid():
            profile_form.save()
            return redirect('index')
    else:
        profile_form = PersonalinfoForm(instance=request.user)
    return render(request, 'personal_info.html',{ "profile_form": profile_form})