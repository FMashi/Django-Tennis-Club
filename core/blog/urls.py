from django.urls import path,re_path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('posts/', views.post_list, name='post_list'),
    path('comments/', views.comment_list, name='comment_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('users/', views.user_list, name='user_list'),
]
