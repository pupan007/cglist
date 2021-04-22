from django.urls import path
from .views import template1, template2

urlpatterns = [
    path('template1', template1, name = 'template1'),
    path('template2', template2, name = 'template2'),
    
]
