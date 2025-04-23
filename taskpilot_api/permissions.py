from rest_framework import permissions


class IsOwnerOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a task to view or edit it.
    Unauthenticated users or non-owners get no access.
    """

    def has_object_permission(self, request, view, obj):
        # First check if the user is authenticated
        if not request.user or not request.user.is_authenticated:
            return False

        # Then check if the object belongs to the user
        return obj.owner == request.user
