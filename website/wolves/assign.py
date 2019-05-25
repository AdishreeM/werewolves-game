from .models import Room, Player
import random


roles_c2i = {'Unassigned':0, 'Moderator':1, 'Doctor':2,
                'Seer':3, 'Werewolves':4, 'Villager':5}

def assign(room_name, role_dict):
    roles = []
    for d in role_dict:
        for _ in range(role_dict[d]):
            roles.append(roles_c2i[d])
    random.shuffle(roles)
    players = Player.objects.filter(room__name=room_name, role=0)
    for p,r in zip(players, roles):
        p.role = r
        p.save()
    room = Room.objects.get(name = room_name)
    room.assigned = 1
    room.save()