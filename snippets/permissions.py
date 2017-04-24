from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Always allow GET, HEAD, and OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write perms only for owner
        return obj.owner == request.user
