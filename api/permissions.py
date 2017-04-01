from rest_framework import permissions
from rest_framework.compat import is_authenticated


class AllowAllForGet(permissions.BasePermission):


    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        return request.user and is_authenticated(request.user)
