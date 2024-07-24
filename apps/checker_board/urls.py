from rest_framework.routers import DefaultRouter

from apps.checker_board.views import (
    BoardView,
    MissionView,
    ActionView,
    DailyStatisticsView,
)

router = DefaultRouter()
router.register(r"boards", BoardView, basename="board")
router.register(r"missions", MissionView, basename="mission")
router.register(r"actions", ActionView, basename="action")
router.register(r"daily_statistics", DailyStatisticsView, basename="daily_statistics")


urlpatterns = router.urls
