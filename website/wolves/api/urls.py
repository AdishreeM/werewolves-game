from django.urls import path
from .views import RoomViewSet

urlpatterns = [
    # Availability check
    path('rooms/<str:roomName>', RoomViewSet.as_view({'get': 'retrieve'}), name='room_exists'),

    # Room
    # path('rooms/<st:roomname>', view2, name='room'),

    # Room role assign
    # path('rooms/<str:roomname>/assign', view3, name='room_assign'),

    # Create


    # Join
]