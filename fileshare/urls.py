from django.urls import path

from . import views


app_name = 'fileshare'

urlpatterns = [ 
    path('', views.index, name='index'),
    path('receive-file/', views.receive, name='receive'),
]