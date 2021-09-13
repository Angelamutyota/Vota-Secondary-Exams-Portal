# from votapp.views import teacher_register
from votapp.models import Personalinfo, Student, Teacher
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


User = get_user_model()
class PersonalinfoForm(forms.ModelForm):
    class Meta:
        model = Personalinfo
        fields = ['user', 'picture', 'gender', 'admno', 'parent_contact']

class TeacherRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields =  ['username','email','password1','password2']
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.save()
        return user

class StudentRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','password1','password2']

    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.save()
        return user        