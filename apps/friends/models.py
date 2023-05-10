from enum import auto

from django.db import models

from apps.authentication.models import User
from friends_service import settings


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='friend_requests_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='friend_requests_received', on_delete=models.CASCADE)
    is_friends = models.BooleanField(default=False)

    def __str__(self):
        return f"ID: {self.id}. From: {self.from_user}. To: {self.to_user}."

    class Meta:
        unique_together = ('from_user', 'to_user')
