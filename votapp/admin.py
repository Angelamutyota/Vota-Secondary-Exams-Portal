from django.contrib import admin
from .models import teacher, student, StudentExtra, Subject, User
# Register your models here.

admin.site.register(teacher)
admin.site.register(student)
admin.site.register(Subject)
admin.site.register(StudentExtra)
admin.site.register(User)