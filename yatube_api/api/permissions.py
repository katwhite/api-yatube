from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Чтение (GET) разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Изменение (PUT, PATCH, DELETE) только автору
        return obj.author == request.user