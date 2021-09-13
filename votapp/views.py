
from votapp.forms import PersonalinfoForm, StudentRegistrationForm, TeacherRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render

def tdash(request):
    return render(request, 'tdash.html')

def index(request):
    return render(request, 'dash.html')

def exam1 (request):
      return render(request, 'exam1.html')

def exam2 (request):
      return render(request, 'exam2.html')

def endterm (request):
      return render(request, 'endterm.html')

def finalreport (request):
      return render(request, 'finalreport.html')

class teacher_register(CreateView):
    model = User
    form_class = TeacherRegistrationForm
    template_name = "teacher_register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("login")

class student_register(CreateView):
    model = User
    form_class = StudentRegistrationForm
    template_name = "student_register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("login")

@csrf_exempt
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_authenticated and request.user.is_teacher:
                    teachers = "<h2>vota teachers </h2>"
                    return render(request,'index.html')
                else:
                    students="<h2>Vota students </h2>"
                return render(request,'index.html')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html", {"form": AuthenticationForm})


def logout_request(request):
    logout(request)
    return redirect("login")        


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


