from rest_framework import permissions


class IsOwnerOnly(permissions.BasePermission):
    """
    Custom permission to allow only the owner of a task to access or modify it.
    - Unauthenticated users are denied at the view level.
    - Authenticated users are allowed only if they own the object.
    """

    def has_permission(self, request, view):
        # Deny access entirely if user is not authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow access only if the object's owner matches the request user
        return getattr(obj, 'owner', None) == request.user
