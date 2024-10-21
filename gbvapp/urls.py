from django.urls import path, include
from . import views
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView





urlpatterns = [

    
    path('', views.homepage, name='homepage'),
    path('reportincident/', views.reportincident, name='reportincident'),
    path('supportservices/', views.supportservices, name='supportservices'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('collect_email/', views.collect_email, name='collect_email'),
]
