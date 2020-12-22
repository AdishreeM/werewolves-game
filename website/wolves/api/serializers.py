from ..models import Room, Player
from django.contrib.auth.models import User
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):

    class PlayerSerializer(serializers.ModelSerializer):
        name = serializers.CharField(source="user.username")
        class Meta:
            model = Player
            fields = ['name', 'role']

    def player_is_moderator(self, room):
        return self.context['player'].role == 1

    players = PlayerSerializer(many=True)
    you_are_moderator = serializers.SerializerMethodField('player_is_moderator')

    class Meta:
        model = Room
        fields = ['players', 'name', 'assigned', 'you_are_moderator']
