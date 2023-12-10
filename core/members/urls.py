from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.members_list, name='members_list'),
    path('<str:member_id>/', views.member_detail, name='member_detail'),
]
