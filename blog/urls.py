from django.urls import path
from . import views
from .views import PostListView, PostDetailView, add_post

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),

    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('add/', add_post, name='add_post'),
]