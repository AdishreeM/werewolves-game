from .models import Room, Player
import random

roles_i2c = {0:'Unassigned', 1:'Moderator', 2:'Doctor',
                3:'Seer', 4:'Werewolves', 5:'Villager'}
roles_c2i = {'Unassigned':0, 'Moderator':1, 'Doctor':2,
                'Seer':3, 'Werewolves':4, 'Villager':5}

def assign(room_name, dict):
    roles = []
    for d in dict:
        for _ in range(dict[d]):
            roles.append(roles_c2i[d])
    random.shuffle(roles)
    players = Player.objects.filter(room__name=room_name, role=0)
    i = 0
    for p in players:
        p.role = roles[i]
        p.save()
        i += 1