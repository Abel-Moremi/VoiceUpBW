from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('<str:username>/feed/', views.feed, name='feed'),
    path('<int:id>/', views.post_detail, name="detail"),
]
