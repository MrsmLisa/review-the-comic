from django.urls import path 
from . import path

urlpatterns = [
    path('', views.index, name='index')
]