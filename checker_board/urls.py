from rest_framework.routers import DefaultRouter

from checker_board.views import BoardView

router = DefaultRouter()
router.register(r"boards", BoardView, basename="board")

urlpatterns = router.urls
