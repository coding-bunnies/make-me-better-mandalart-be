from rest_framework import serializers

from apps.checker_board.models import Board, Mission, Action, DailyStatistics


class BoardSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    achievement = serializers.IntegerField(read_only=True)
    deleted = serializers.DateTimeField(read_only=True)

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
            "mission_id",
            "position",
            "title",
            "period",
            "goal_unit",
            "action_unit",
            "current_unit",
            "achievement",
            "unit_name",
            "deleted",
            "completed_at",
        )


class MissionRetrieveSerializer(serializers.ModelSerializer):
    actions = ActionSerializer(many=True, read_only=True)

    class Meta:
        model = Mission
        fields = (
            "id",
            "title",
            "actions",
        )


class BoardRetrieveSerializer(serializers.ModelSerializer):
    missions = MissionRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = (
            "id",
            "title",
            "start_at",
            "end_at",
            "missions",
            "daily_goal",
            "total_percentage",
        )


class DailyStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyStatistics
        fields = (
            "id",
            "percentage",
        )
