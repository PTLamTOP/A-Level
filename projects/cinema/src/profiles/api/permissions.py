from rest_framework import permissions
from .exceptions import InvalidAction


class IsNotAuthenticated(permissions.BasePermission):
    """
    Custom permission to only allow admin to create and edit.
    """
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return True
        raise InvalidAction

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return True
        raise InvalidAction