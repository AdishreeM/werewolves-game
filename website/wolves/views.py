from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player, Room 
from .namegen.generator import generate
# Create your views here.

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
                        i = 0
                        while i<4:
                            room_name = generate()
                            if Room.objects.filter(name=room_name).exists():
                                i += 1
                            else:
                                flag = 0
                                break
                    if flag == 1:
                        return HttpResponse("Sorry, we are facing heavy traffic. Try again later :/")
                    else:
                        new_room = Room(name=room_name)
                        new_room.save()
                        new_player = Player(user=request.user, room=new_room, role=1)
                        new_player.save()
                
                    redirect(room)

                # Join a room
                else:
                    room_name = request.POST.get('room_name')
                    if Room.objects.filter(name=room_name).exists():
                        redirect(room)
                    else:
                        return HttpResponse("No such room exists o.0")
        
        # Already belongs to a room
        else:
            return redirect('room')        

def room(request):
    name = request.user.username
    room = request.user.player.room.name
    msg = 'Hi '+name+'! You are in Room: ' + room
    return HttpResponse(msg)