from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('room', views.RoomView.as_view(), name='room'),
    path('table', views.table, name='table'),
    path('role', views.role, name='role')
]