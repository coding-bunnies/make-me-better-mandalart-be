from rest_framework import serializers

from checker_board.models import Board, Mission, Action


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


class ActionSerializer(serializers.ModelSerializer):
    mission_id = serializers.IntegerField()

    class Meta:
        model = Action
        fields = (
            "id",
            "title",
            "mission_id",
            "cycle",
            "goal_unit",
            "action_unit",
            "unit_name",
        )
