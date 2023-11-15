from django.contrib import admin
from django.urls import path

from blog.views import PostListView, PostCreateView, PostDetailView

urlpatterns = [
    path('',PostListView.as_view(), name="blog"),
    path('create-post/',PostCreateView.as_view(), name="create-post"),
    path('<int:pk>/',PostDetailView.as_view(), name="detail-post"),
]