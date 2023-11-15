from django.contrib import admin
from django.urls import path

from blog.views import PostListView, PostCreateView

urlpatterns = [
    path('',PostListView.as_view(), name="blog"),
    path('create-post/',PostCreateView.as_view(), name="create-post"),
]