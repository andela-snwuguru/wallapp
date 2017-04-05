from django.contrib import admin
from api.models import Wall, PostLike


@admin.register(Wall)
class WallAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'date_created']


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'wall', 'date_created']
