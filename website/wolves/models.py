from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=200)
    assigned = models.BooleanField(default = False)

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name='players')
    role = models.IntegerField(default = 0)

    def is_moderator(self):
        return self.role == 1
