from . import views
from django.urls import path

urlpatterns = [
    path('review/<slug:slug>/', views.review_detail, name='review_detail'),
    path('', views.ReviewListView.as_view(), name='index'),
    path('review_create/', views.review_create, name='review_create'),
    path('review/<slug:slug>/comment/', views.comment_review, name='comment_review'),
    path('review/<slug:slug>/like/', views.review_like, name='review_like'),
    path('edit_review/<slug:slug>/', views.editPost, name='edit_review'),
    path('delete_review/<slug:slug>/', views.deletePost, name='delete_review'),
]
