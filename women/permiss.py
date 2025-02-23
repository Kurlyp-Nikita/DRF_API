from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # если метод безопасный, то даём доступ для всех пользователей
        if request.method in permissions.SAFE_METHODS:  # SAFE_METHODS в этом методе запросы только для чтения
            return True

        # иначе только, для админа
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
     Разрешение на уровне объекта, позволяющее редактировать объект только его владельцам.
     Предполагается, что экземпляр модели имеет атрибут `owner`.
     """

    def has_object_permission(self, request, view, obj):
        # Разрешения на чтение разрешены для любого запроса,
        # поэтому мы всегда будем разрешать запросы GET, HEAD или OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Экземпляр должен иметь атрибут с именем `owner`.
        return obj.user == request.user

