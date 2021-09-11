from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name = 'index'),
    path('tdash/', views.tdash, name='tdash'),
    path('exam1/', views.exam1, name='exam1'),
    path('exam2/', views.exam2, name='exam2'),
    path('endterm/', views.endterm, name='endterm'),
    path('finalreport/', views.finalreport, name='finalreport'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)