from django.contrib import admin
from django.urls import path

from blog.views import PostListView, PostCreateView, PostDetailView, PostFilterByAutor, PostUpdateView, PostDeleteView

urlpatterns = [
    path('',PostListView.as_view(), name="blog"),
    path('create-post/',PostCreateView.as_view(), name="create-post"),
    path('<int:pk>/',PostDetailView.as_view(), name="detail-post"),
    path('mis-posts/',PostFilterByAutor, name="mis-posts"),
    path('mis-posts/edit/<int:pk>/',PostUpdateView.as_view(), name="edit-post"),
    path('mis-posts/delete/<int:pk>/',PostDeleteView.as_view(), name="delete-post"),
]