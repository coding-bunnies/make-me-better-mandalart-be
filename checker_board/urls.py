from rest_framework.routers import DefaultRouter

from checker_board.views import BoardView, MissionView

router = DefaultRouter()
router.register(r"boards", BoardView, basename="board")
router.register(r"missions", MissionView, basename="mission")

urlpatterns = router.urls
