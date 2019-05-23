from django.db import models
from django.contrib.auth.models import User

# Create your models here.

roles_i2c = {0:'Unassigned', 1:'Moderator', 2:'Doctor',
                3:'Seer', 4:'Werewolves', 5:'Villager'}
roles_c2i = {'Unassigned':0, 'Moderator':1, 'Doctor':2,
                'Seer':3, 'Werewolves':4, 'Villager':5}

class Room(models.Model):
    name = models.CharField(max_length=200)

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    role = models.IntegerField(default = 0)
