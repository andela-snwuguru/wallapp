from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Wall(models.Model):
    user = models.ForeignKey(User, related_name="walls")
    message = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.message
