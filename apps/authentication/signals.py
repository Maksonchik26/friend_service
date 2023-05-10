from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.authentication.models import User
