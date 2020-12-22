from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from ..models import Room, Player
from .serializers import RoomSerializer
from .permissions import IsInRoom
from ..assign import assign as assignRoles

class RoomViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsInRoom]

    def retrieve(self, request, roomName):
        queryset = Room.objects.all()
        room = get_object_or_404(queryset, name=roomName)
        self.check_object_permissions(request, room)
        serializer = RoomSerializer(
            room, context={'player': request.user.player})
        return Response(serializer.data)

    def exists(self, request, roomName):
        try:
            Room.objects.get(name=roomName)
            return Response({"name": roomName, "exists": True})
        except Room.DoesNotExist:
            return Response({"name": roomName, "exists": False})

    def assign(self, request, roomName):
        if request.user.player.is_moderator():
            room = get_object_or_404(Room.objects.all(), name=roomName)
            player_count = len(Player.objects.filter(room=room))
            if player_count < 5:
                return Response({"assigned": False, "message": "Less than 5 players"})

            wolves = player_count//3
            player_count -= wolves

            seer = 1
            player_count -= seer

            doctor = 1
            player_count -= doctor

            villagers = player_count

            role_dict = {
                2: doctor,
                3: seer,
                4: wolves,
                5: villagers
            }
            assignRoles(Room.name, role_dict)
            return Response({"assigned": True})

        else:
            return HttpResponseForbidden()
