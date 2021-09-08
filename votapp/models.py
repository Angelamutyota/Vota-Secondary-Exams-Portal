
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
  

class student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)


    def __str__(self):
        return self.user.username

class teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self):
        return self.user.username


classes = [('form-one', 'form-one'),
           ('form-two', 'form-two'),
           ('form-three', 'form-three'),
           ('form-four', 'form-four')]
           
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    feeball=models.PositiveIntegerField(null=True)
    nextfees=models.PositiveIntegerField(null=True)
    form= models.CharField(max_length=10,choices=classes,default='form-one')
    meangrade=models.
    totalmaks=
    meanmark=
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name