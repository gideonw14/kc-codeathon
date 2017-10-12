"""
Definition of models.
"""
from django.db import models
from django.contrib.auth.models import User, AnonymousUser



class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=64)
    key_expires = models.DateTimeField()

    def __str__(self):
        return self.user.username
