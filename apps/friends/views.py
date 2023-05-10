from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.decorators import action

from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import FriendRequestSerializer
from ..authentication.models import User
from apps.friends.models import FriendRequest
from ..authentication.serializers import UserSerializer


@login_required
def send_friend_request(request, user_id):
    from_user = request.user
    to_user = User.objects.get(id=user_id)
    friend_request, created = FriendRequest.objects.get_or_create(
        from_user=from_user, to_user=to_user)
    if FriendRequest.objects.filter(from_user=to_user, to_user=from_user).exists():
        from_user.friends.add(to_user)
        to_user.friends.add(from_user)
        friend_request.is_friends = True
        friend_request.save()
        return HttpResponse('Added to friends')
    elif created:
        return HttpResponse('Friend request sent')
    else:
        return HttpResponse(' ')


@login_required
def accept_friend_request(request, request_id):
    friend_request = FriendRequest.objects.get(id=request_id)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.is_friends = True
        friend_request.save()
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('friend request not accepted')


@login_required
def reject_friend_request(request, request_id):
    friend_request = FriendRequest.objects.get(id=request_id)
    if friend_request.to_user == request.user and friend_request.is_friends == False:
        friend_request.delete()
        return HttpResponse('Friend request rejected')
    else:
        return HttpResponse('Request does not exist')


@login_required
def request_status(request, user_id):
    target_user = User.objects.filter(id=user_id).first()
    if target_user in request.user.friends.all():
        return HttpResponse("Already friends")
    elif FriendRequest.objects.filter(from_user=request.user, to_user=target_user).exists():
        return HttpResponse("Outgoing request")
    elif FriendRequest.objects.filter(from_user=target_user, to_user=request.user).exists():
        return HttpResponse("Incoming request")
    else:
        return HttpResponse("Nothing")


@login_required
def delete_friend(request, user_id):
    target_user = User.objects.filter(id=user_id).first()
    if target_user in request.user.friends.all():
        request.user.friends.remove(target_user)
        target_user.friends.remove(request.user)
        return HttpResponse("Deleted")
    else:
        return HttpResponse("You are not friends. Can not delete")



# class FriendRequestViewSet(viewsets.ModelViewSet):
#     queryset = FriendRequest.objects.all()
#     serializer_class = FriendRequestSerializer
#
#     def get(self, request):
#         incoming_requests = FriendRequest.objects.filter(to_user=request.user, is_friends=0)
#         outgoing_requests = FriendRequest.objects.filter(from_user=request.user, is_friends=0)
#         return Response(
#             {'incoming_requests': FriendRequestSerializer(incoming_requests, many=True).data,
#              'outgoing_requests': FriendRequestSerializer(outgoing_requests, many=True).data})
#
#     @action(methods=["GET"], detail=True)
#     def create(self, request, user_id, *args, **kwargs):
#         from_user = request.user
#         to_user = User.objects.get(id=user_id)
#         friend_request, created = FriendRequest.objects.get_or_create(
#             from_user=from_user, to_user=to_user)
#         if FriendRequest.objects.filter(from_user=to_user, to_user=from_user).exists():
#             from_user.friends.add(to_user)
#             to_user.friends.add(from_user)
#             friend_request.is_friends = True
#             friend_request.save()
#             return HttpResponse('Add to friends')
#         elif created:
#             return HttpResponse('friend request sent')
#         else:
#             return HttpResponse('friend request has already sent')


#НУЖНОООО
class FriendsAPIView(APIView):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        friends = user.friends.all()
        return Response(
            {'friends': UserSerializer(friends, many=True).data})

class FriendRequestAPIView(APIView):
    def get(self, request):
        incoming_requests = FriendRequest.objects.filter(to_user=request.user, is_friends=0)
        outgoing_requests = FriendRequest.objects.filter(from_user=request.user, is_friends=0)
        return Response(
            {'incoming_requests': FriendRequestSerializer(incoming_requests, many=True).data,
             'outgoing_requests': FriendRequestSerializer(outgoing_requests, many=True).data})