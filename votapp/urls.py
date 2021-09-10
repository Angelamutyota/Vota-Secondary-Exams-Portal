from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('personalinfo/', views.personal_info, name='personalinfo'),
    url('student_register/', views.student_register.as_view(),
        name='student_register'),
    url('teacher_register/', views.teacher_register.as_view(),
        name='teacher_register'),
    url('login/', views.login_request, name='login'),
    url('logout/', views.logout_request, name='logout'),

]
