from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Player, Room 
from .namegen.generator import generate
from .assign import assign

roles_i2c = {0:'Unassigned', 1:'Moderator', 2:'Doctor', 3:'Seer', 4:'Werewolves', 5:'Villager'}

def index(request):
    # User not signed in
    if not request.user.is_authenticated:
        return render(request, 'wolves/index.html')
    
    # User signed in
    else:
        # Room doesn't exist
        if not hasattr(request.user, 'player'):
            if request.method == 'GET':
                return render(request, 'wolves/user.html')
            else:
                # Create a room -> Moderator
                if request.POST.get('choice') == 'create': 
                    room_name = generate()
                    flag = 0
                    if Room.objects.filter(name=room_name).exists():
                        flag = 1
                        for _ in range(4):
                            room_name = generate()
                            if not Room.objects.filter(name=room_name).exists():
                                flag = 0
                                break
                    if flag == 1:
                        return HttpResponse("Sorry, we are facing heavy traffic. Try again later :/")
                    else:
                        new_room = Room(name=room_name, assgned = False)
                        new_room.save()
                        new_player = Player(user=request.user, room=new_room, role=1)
                        new_player.save()
                
                    return redirect(room)

                # Join a room
                else:
                    room_name = request.POST.get('room_name')
                    if Room.objects.filter(name=room_name).exists():
                        if not Player.objects.filter(user=request.user).exists():
                            room_to_join = Room.objects.get(name=room_name)
                            new_player = Player(user=request.user, room=room_to_join, role=0)
                            new_player.save()
                        return redirect(room)
                    else:
                        return HttpResponse("No such room exists o.0")
        
        # Already belongs to a room
        else:
            return redirect('room')        

def room(request):
    if request.method == 'POST' and request.user.player.role == 1: # Moderator
            role_dict = {2:request.POST.get('doctor'), 3:request.POST.get('seer'),
                             4:request.POST.get('wolf'), 5:request.POST.get('villager') }
            assign(request.user.player.room.name, role_dict)
            return render(request, 'wolves/moderator_room.html')
    else:
        if request.user.player.role == 1:
            return render(request, 'wolves/moderator_room.html')
        else:
            return render(request, 'wolves/other_room.html', {'roles': roles_i2c})

def table(request):
    players = request.user.room.players
    return render(request, 'wolves/room_table.html', {'players': players})

def role(request):
    present_role = request.user.player.role
    data = {'role': roles_i2c[present_role]}
    return JsonResponse(data)
    
