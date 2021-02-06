from rest_framework.permissions import SAFE_METHODS, BasePermission


class CustomerAccessPermission(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return any([
            request.method in SAFE_METHODS,
            obj.author == request.user,
            request.user.is_authenticated and (
                    request.user.is_moderator or request.user.is_admin),
        ])
