from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from checker_board.models import Board, Mission
from checker_board.serializers import BoardSerializer, MissionSerializer


# Create your views here.
class BoardView(ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
    permission_classes = (IsAuthenticated,)


class MissionView(ModelViewSet):
    serializer_class = MissionSerializer
    queryset = Mission.objects.all()
    permission_classes = (IsAuthenticated,)
