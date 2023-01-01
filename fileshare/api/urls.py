from django.urls import path

from . import views

urlpatterns = [
    path('', views.FileReceiveView.as_view(), name='file-receive'),
    path('serve-file/', views.FileServeView.as_view(), name='file-serve'),
]