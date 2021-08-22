from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Curstom permission to only allow owners of an object to delete it
    """

    def has_object_permission(self, request, view, obj):
        # Read only permissions are allowed to any request,
        # so we'll allways allow GET, HEAD or OPTIONS request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # write permissions are only allowed to the owner of the snippet
        return obj.owner == request.user
        