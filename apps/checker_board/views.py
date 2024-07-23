from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.checker_board.models import Board, Mission, Action
from apps.checker_board.serializers import (
    BoardSerializer,
    BoardRetrieveSerializer,
    MissionSerializer,
    ActionSerializer,
)


# Create your views here.
class BoardView(ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
    permission_classes = (IsAuthenticated,)

    @extend_schema(responses=BoardRetrieveSerializer)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BoardRetrieveSerializer(instance)
        return Response(serializer.data)


class MissionView(ModelViewSet):
    serializer_class = MissionSerializer
    queryset = Mission.objects.all()
    permission_classes = (IsAuthenticated,)


class ActionView(ModelViewSet):
    serializer_class = ActionSerializer
    queryset = Action.objects.all()
    permission_classes = (IsAuthenticated,)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increase_achievement()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
