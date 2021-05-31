from django.urls import path
from .views import template2, Create_CV

urlpatterns = [
    path('template1', Create_CV.as_view(), name = 'CV_1'),
    path('template2', template2, name = 'template2'),
    
]
