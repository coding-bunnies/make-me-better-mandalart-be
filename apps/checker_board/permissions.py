from rest_framework.permissions import IsAuthenticated, BasePermission


class IsMeOnly(IsAuthenticated):

    def has_permission(self, request, view):
        return (
            super().has_permission(request, view)
            and request.user == view.get_object().board.user
        )

    # def has_object_permission(self, request, view, obj):
    #     return obj.board.user == request.user
