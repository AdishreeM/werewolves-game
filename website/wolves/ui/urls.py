from django.urls import path
from .views import UiView

urlpatterns = [
    path('*', UiView),
]