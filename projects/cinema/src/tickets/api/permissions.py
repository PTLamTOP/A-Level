from rest_framework import permissions


class IsAdminOrReadAndBuyOnly(permissions.BasePermission):
    """
    Standard user can read and buy tickets.
    Admin can do everything.
    """
    def has_object_permission(self, request, view, obj):
        # Permission that only admin can do not safe HTTP requests.
        if request.user.is_superuser:
            return True
        # standard user can read and buy ticket
        if request.method in ('GET', 'HEAD', 'OPTIONS',):
            return True

    def has_permission(self, request, view):
        # Permission that only admin can do not safe HTTP requests.
        if request.user.is_superuser:
            return True
        # standard user can read and buy ticket
        if request.method in ('GET', 'HEAD', 'OPTIONS', 'POST',):
            return True