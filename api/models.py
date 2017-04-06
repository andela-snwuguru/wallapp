from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Wall(models.Model):
    user = models.ForeignKey(User, related_name="walls")
    message = models.TextField()
    image = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


class PostLike(models.Model):
    user = models.ForeignKey(User, related_name="likes")
    wall = models.ForeignKey(Wall, related_name="likes")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'wall'),)

    def __str__(self):
        return self.wall.message


class PostComment(models.Model):
    user = models.ForeignKey(User, related_name="comments")
    wall = models.ForeignKey(Wall, related_name="comments")
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
