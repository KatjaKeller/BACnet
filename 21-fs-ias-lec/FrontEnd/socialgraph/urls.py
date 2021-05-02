from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='socialgraph-home'),
    path('users/', views.users, name='socialgraph-users'),
    path('about/', views.about, name='socialgraph-about'),
    path('feed/', views.feed, name='socialgraph-feed'),
    path('profile/<pk>/', views.PostDetailView.as_view(), name='profile-detail'),
]