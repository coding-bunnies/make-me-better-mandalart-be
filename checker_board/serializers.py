from rest_framework import serializers

from checker_board.models import Board, Mission


class BoardSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Board
        fields = "__all__"


class MissionSerializer(serializers.ModelSerializer):
    board_id = serializers.IntegerField()

    class Meta:
        model = Mission
        fields = (
            "id",
            "title",
            "board_id",
        )
