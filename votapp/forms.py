from votapp.models import Personalinfo
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PersonalinfoForm(forms.ModelForm):
    class Meta:
        model = Personalinfo
        fields = ['user', 'picture', 'gender', 'admno', 'parent_contact']