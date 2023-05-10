from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.authentication.models import User
from apps.authentication.serializers import UserSerializer
from apps.friends.models import FriendRequest


class FriendRequestSerializer(serializers.ModelSerializer):
    from_user = UserSerializer()
    to_user = UserSerializer()

    class Meta:
        model = FriendRequest
        fields = ('id', 'from_user', 'to_user', 'is_friends')
