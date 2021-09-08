from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

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


lessons = [('English', 'English'),
           ('Kiswahili', 'Kiswahili'),
           ('Maths', 'Maths'),
           ('Chemistry', 'Chemistry'),
           ('Biology', 'Biology'),
           ('Physics','Physics'),
           ('C.R.E', 'C.R.E'),
           ('History and Government', 'History and Government'),
           ('Geography','Geography'),
           ('Business Studies','Business Studies'),
           ('Agriculture','Agriculture')]

grades = [('A','A'),
        ('A-','A-'),
        ('B+','B+'),
        ('B','B'),
        ('B-','B-'),
        ('C+','C+'),
        ('C','C'),
        ('C-','C-'),
        ('D+','D+'),
        ('D','D'),
        ('D-','D-'),
        ('E','E'),
        ]

Exams = [('Exam 1','Exam 1'),
        ('Exam 2', 'Exam 2'),
        ('End term','End term'),
        
        ]

remark = [('Excellent','Excellent'),
        ('Very Good', 'Very Good'),
        ('Good','Good'),
        ('Average','Average'),
        ('Put more effort', 'Put more effort'),
        ('Poor','Poor'),
        
        ]

        
        

           

class Subject(models.Model) :
    subject=models.CharField(max_length=1000,choices=lessons, default='none')
    marks=models.IntegerField(null=True, blank=True)
    grade=models.CharField(max_length=100,choices=grades, default='E')
    examinations = models.CharField(max_length=100, choices=Exams,default='0')
    points=models.IntegerField(null=True, blank=True)
    position= models.IntegerField(null=True, blank=True)
    remarks = models.CharField(max_length=1000, choices=remark, default='none')
    initials= models.CharField(max_length=100)


classes = [('form-one', 'form-one'),
           ('form-two', 'form-two'),
           ('form-three', 'form-three'),
           ('form-four', 'form-four')]

grades = [('A','A'),
        ('A-','A-'),
        ('B+','B+'),
        ('B','B'),
        ('B-','B-'),
        ('C+','C+'),
        ('C','C'),
        ('C-','C-'),
        ('D+','D+'),
        ('D','D'),
        ('D-','D-'),
        ('E','E'),
        ]

           
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    feeball=models.PositiveIntegerField(null=True, blank=True)
    nextfees=models.PositiveIntegerField(null=True, blank=True)
    form= models.CharField(max_length=10,choices=classes,default='form-one')
    meangrade=models.CharField(max_length=100,choices=grades, default='E')
    totalmaks=models.IntegerField(null=True, blank=True)
    meanmark=models.IntegerField(null=True, blank=True)
    subjects=models.ForeignKey(Subject,on_delete=models.CASCADE, related_name='sub')
    admno=models.IntegerField(null=True, blank=True)
    hse=models.CharField(max_length=1000)

   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Personalinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='0')
    picture = CloudinaryField('image')
    gender = models.TextField(max_length=10)
    admno = models.IntegerField(null=True, blank=True)
    parent_contact = models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.user.username


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()