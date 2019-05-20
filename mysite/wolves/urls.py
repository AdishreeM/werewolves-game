from django.urls import path
from core import views as core_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]