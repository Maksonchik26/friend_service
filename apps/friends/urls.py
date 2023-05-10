from django.urls import path, include, re_path
from rest_framework_nested import routers

from . import views
from .views import *

urlpatterns = [
    path('send-request/<int:user_id>/', send_friend_request, name='send_friend_request'),
    path('accept-request/<int:request_id>/', accept_friend_request, name='accept_friend_request'),
    path('requestlist/', FriendRequestAPIView.as_view(), name='request_list'),
    path('reject-request/<int:request_id>/', reject_friend_request, name='reject_friend_request'),
    path('request-status/<int:user_id>/', request_status, name='friendship_status'),
    path('delete-friend/<int:user_id>/', delete_friend, name='delete_friend'),
    path('friendslist/', FriendsAPIView.as_view(), name='friend_list'),
]
