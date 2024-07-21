from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from checker_board.models import Board
from checker_board.serializers import BoardSerializer


# Create your views here.
class BoardView(ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
    permission_classes = (IsAuthenticated,)
