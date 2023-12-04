from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members_list, name='members_list'),
    path('members/<int:members_id>/', views.member_detail, name='member_detail'),
]
