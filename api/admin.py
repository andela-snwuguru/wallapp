from django.contrib import admin
from api.models import Wall


@admin.register(Wall)
class WallAdmin(admin.ModelAdmin):
    list_display = ['user', 'message']
