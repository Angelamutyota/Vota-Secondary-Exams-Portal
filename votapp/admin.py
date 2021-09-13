from django.contrib import admin
from .models import Teacher, Student, StudentExtra, Subject, User
# Register your models here.

from .models import Teacher, Student, StudentExtra, Subject, User, Personalinfo

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(StudentExtra)
admin.site.register(User)
admin.site.register(Personalinfo)
