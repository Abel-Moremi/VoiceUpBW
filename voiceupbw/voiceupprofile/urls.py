from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('signout/', views.signout, name='signout'),
    path('<str:username>/follows/', views.follows, name='follows'),
    path('<str:username>/followers/', views.followers, name='following'),
    path('<str:username>/follow/', views.follow, name='follow'),
    path('<str:username>/stopfollow/', views.stopfollow, name='stopfollow'),
    path('<str:username>/', views.profile, name="profile"),
]
