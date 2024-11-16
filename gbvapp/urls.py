from django.urls import path
from . import views


urlpatterns = [    
    path('', views.homepage, name='homepage'),
    path('reportincident/', views.reportincident, name='reportincident'),
    path('supportservices/', views.supportservices, name='supportservices'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('collect_email/', views.collect_email, name='collect_email'),
    path('dropdown/', views.dropdown, name='dropdown'),
]
