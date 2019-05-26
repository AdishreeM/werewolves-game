from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.views import View
from .models import Player, Room 
from .namegen.generator import generate
from .assign import assign

roles_i2c = {0:'Unassigned', 1:'Moderator', 2:'Doctor', 3:'Seer', 4:'Werewolves', 5:'Villager'}


class IndexView(View):

    def get(self, request):
        
        # Anonymous user
        if not request.user.is_authenticated:
            return render(request, 'wolves/index_anon.html')
        
        # Authenticated user
        else:
            # Doesn't have a player (and therefore a room),
            if not hasattr(request.user, 'player'):
                return render(request, 'wolves/index_authed.html')
            # Has a player (and a room)
            else:
                return redirect('room')

    def post(self, request):

        # Can't create room if anonymous
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        # Is authenticated
        else:
            # Create a room
            if request.POST.get('choice') == 'create': 
                
                for _ in range(5):
                    room_name = generate()
                    try:
                        Room.objects.get(name=room_name)
                        continue
                    except Room.DoesNotExist:
                        Player.objects.update_or_create(
                            user=user,
                            defaults={'room': Room.objects.create(name=room_name),
                                      'role': 1}
                        )

            # Join a room
            else:
                try:
                    room = Room.objects.get(name=request.POST.get('room_name'))
                except Room.DoesNotExist:
                    return HttpResponse("No such room exists o.0")
                
                Player.objects.update_or_create(user=request.user, defaults={'room': room})

            # In both cases, redirected to room
            return redirect('room')


class RoomView(View):

    def get(self, request):
        # User is moderator
        if request.user.player.role == 1:
            return render(request, 'wolves/room_mod.html')

        # User is player
        else:
            return render(request, 'wolves/room_player.html', {'roles': roles_i2c})

    
    def post(self, request):
        # If moderator sent the assignment dict, assign and
        # render the same view
        if request.user.player.is_moderator():
            role_dict = {
                            2:int(request.POST.get('doctor')),
                            3:int(request.POST.get('seer')),
                            4:int(request.POST.get('wolf')),
                            5:int(request.POST.get('villager'))
                        }
            assign(request.user.player.room.name, role_dict)
            return render(request, 'wolves/room_mod.html')

        else:
            return HttpResponseForbidden()


def table(request):
    players = request.user.player.room.players.all()
    return render(request, 'wolves/room_table.html', {'players': players, 'role_dict':roles_i2c})

def role(request):
    present_role = request.user.player.role
    data = {'role': roles_i2c[present_role]}
    return JsonResponse(data)
    
