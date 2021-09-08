from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url('personalinfo/', views.personal_info, name='personalinfo'),
]