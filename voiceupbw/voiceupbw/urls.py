"""voiceupbw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from voiceupprofile import views
from voiceUpPost.views import feed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.frontpage, name='frontpage'),
    path('feed/', feed, name='feed'),
    path('signout/', views.signout, name='signout'),
    path('<str:username>/follows/', views.follows, name='follows'),
    path('<str:username>/followers/', views.followers, name='following'),
    path('<str:username>/follow/', views.follow, name='follow'),
    path('<str:username>/stopfollow/', views.stopfollow, name='stopfollow'),
    path('<str:username>/', views.profile, name="profile"),
]
