from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('tdash/', views.tdash, name='tdash'),
    path('exam1/', views.exam1, name='exam1'),
    path('exam2/', views.exam2, name='exam2'),
    path('endterm/', views.endterm, name='endterm'),
    path('finalreport/', views.finalreport, name='finalreport'),
    url('personalinfo/', views.personal_info, name='personalinfo'),
    url('student_register/', views.student_register.as_view(),
        name='student_register'),
    url('teacher_register/', views.teacher_register.as_view(),
        name='teacher_register'),
    url('login/', views.login_request, name='login'),
    url('logout/', views.logout_request, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

