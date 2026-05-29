from . import views
from django.urls import include, path

urlpatterns = [
    path('review/<slug:slug>/', views.review_detail, name='review_detail'),
    path('', views.ReviewListView.as_view(), name='index'),
]