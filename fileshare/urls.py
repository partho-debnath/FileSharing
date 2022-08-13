from django.urls import path

from . import views


app_name = 'fileshare'

urlpatterns = [ 
    path('', views.index, name='index'),
    path('recive-file/', views.recive, name='recive'),
]