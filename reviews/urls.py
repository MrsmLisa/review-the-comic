from django_summernote import admin

from . import views
from django.urls import include, path

urlpatterns = [
    path('review/<slug:slug>/', views.review_detail, name='review_detail'),
    path('', views.index, name='index'),
]