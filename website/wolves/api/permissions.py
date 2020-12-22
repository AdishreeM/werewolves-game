from rest_framework import permissions

# class IsModerator(permissions.BasePermission):
#     message = 'Moderator permission is required.'

#     def has_obj_permission(self, request, view, room):


class IsInRoom(permissions.BasePermission):
    message = "You need to be in the room"

    def has_object_permission(self, request, view, obj):
        print("IsInRoom.has_obj_permission")
        if hasattr(request.user, 'player') and request.user.player.room == obj:
            print("granting permission")
            return True
        else:
            print("denying permission")
            return False
