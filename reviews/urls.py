from django_summernote import admin
from . import views
from django.urls import include, path

urlpatterns = [
    path('review/<slug:slug>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('', views.ReviewListView.as_view(), name='index'),
]