from datetime import datetime, timedelta

from django.urls import reverse
from rest_framework import status

from apps.checker_board.factories import BoardFactory, MissionFactory, ActionFactory
from apps.checker_board.models import Period
from core.const import DEFAULT_MISSION_COUNT
from core.factories import AccountFactory
from core.tests import BaseAPITestCase


class CheckerBoardBaseTestCase(BaseAPITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = AccountFactory()
        cls.board = BoardFactory.create(user=cls.user)
        cls.missions = MissionFactory.create_batch(
            size=DEFAULT_MISSION_COUNT, board=cls.board
        )
        cls.actions = [
            ActionFactory.create_batch(size=DEFAULT_MISSION_COUNT, mission=mission)
            for mission in cls.missions
        ]


# Create your tests here.
class BoardViewTest(CheckerBoardBaseTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.list_url = reverse("board-list")
        cls.detail_url = reverse("board-detail", args=[cls.board.id])

    def test_get_list(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_unauthenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_retrieve(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_retrieve_unauthenticated(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_create(self):
        self.get_authenticated_user(user=self.user)

        data = {
            "title": "Test Board",
            "start_at": "2021-01-01",
            "end_at": "2021-12-31",
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_unauthenticated(self):
        data = {
            "title": "Test Board",
            "start_at": "2021-01-01",
            "end_at": "2021-12-31",
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_update(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.put(
            path=f"{self.detail_url}",
            data={
                "title": "Updated Board",
                "start_at": "2022-01-01",
                "end_at": "2022-12-31",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_update_unauthenticated(self):
        response = self.client.put(
            path=f"{self.detail_url}",
            data={
                "title": "Updated Board",
                "start_at": "2022-01-01",
                "end_at": "2022-12-31",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_partial_update(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.patch(
            path=f"{self.detail_url}",
            data={
                "title": "Updated Board",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_partial_update_unauthenticated(self):
        response = self.client.patch(
            path=f"{self.detail_url}",
            data={
                "title": "Updated Board",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_destroy(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.delete(path=f"{self.detail_url}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_destroy_unauthenticated(self):
        response = self.client.delete(path=f"{self.detail_url}")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class MissionViewTest(CheckerBoardBaseTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.list_url = reverse("mission-list")
        cls.detail_url = reverse("mission-detail", args=[cls.missions[0].id])

    def test_get_list(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_unauthenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_retrieve(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_retrieve_unauthenticated(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_create(self):
        self.get_authenticated_user(user=self.user)

        data = {
            "title": "Test Mission",
            "board_id": self.board.id,
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_unauthenticated(self):
        data = {
            "title": "Test Mission",
            "board": self.board.id,
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_update(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.put(
            path=f"{self.detail_url}",
            data={
                "title": "Updated Mission",
                "board_id": self.board.id,
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_update_unauthenticated(self):
        response = self.client.put(
            path=f"{self.detail_url}",
            data={
                "title": "Updated Mission",
                "board": self.board.id,
            },
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_partial_update(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.patch(
            path=f"{self.detail_url}",
            data={
                "title": "Updated Mission",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_partial_update_unauthenticated(self):
        response = self.client.patch(
            path=f"{self.detail_url}",
            data={
                "title": "Updated Mission",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_destroy(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.delete(path=f"{self.detail_url}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_destroy_unauthenticated(self):
        response = self.client.delete(path=f"{self.detail_url}")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ActionViewTest(CheckerBoardBaseTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.list_url = reverse("action-list")
        cls.detail_url = reverse("action-detail", args=[cls.actions[0][0].id])

    def test_get_list(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.get(self.list_url)
        print(f"{response.status_code} {response.data=}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_unauthenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_retrieve(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_retrieve_unauthenticated(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_create(self):
        self.get_authenticated_user(user=self.user)

        data = {
            "title": "달리기",
            "mission_id": self.missions[0].id,
            "period": Period.ONCE,
            "goal_unit": 100,
            "action_unit": 10,
            "unit_name": "km",
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_unauthenticated(self):
        data = {
            "title": "Test Action",
            "mission": self.missions[0].id,
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_update(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.put(
            path=f"{self.detail_url}",
            data={
                "title": "달리기",
                "mission_id": self.missions[0].id,
                "period": Period.ONCE,
                "goal_unit": 100,
                "action_unit": 10,
                "unit_name": "km",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_update_unauthenticated(self):
        response = self.client.put(
            path=f"{self.detail_url}",
            data={
                "title": "Updated Action",
                "mission": self.missions[0].id,
            },
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_partial_update(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.patch(path=f"{self.detail_url}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_partial_update_unauthenticated(self):
        response = self.client.patch(
            path=f"{self.detail_url}",
            data={
                "title": "Updated Action",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_destroy(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.delete(path=f"{self.detail_url}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_destroy_unauthenticated(self):
        response = self.client.delete(path=f"{self.detail_url}")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class StatisticsTest(CheckerBoardBaseTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def test_update_total_percentage(self):
        """action.current_unit / action.goal_unit * action_period / total_period"""

        action = self.actions[0][0]

        action.current_unit = 2
        action.goal_unit = 10
        action.period = Period.DAILY
        total_period = timedelta(days=10)

        self.board.start_at = datetime.today()
        self.board.end_at = self.board.start_at + total_period
        self.board.update_total_percentage(action)

        self.assertEqual(self.board.total_percentage, 2.0)

    def test_update_total_percentage_twice(self):
        action = self.actions[0][0]

        action.current_unit = 2
        action.goal_unit = 10
        action.period = Period.DAILY
        total_period = timedelta(days=10)

        self.board.start_at = datetime.today()
        self.board.end_at = self.board.start_at + total_period

        self.board.update_total_percentage(action)
        self.board.update_total_percentage(action)

        self.assertEqual(self.board.total_percentage, 4)

    def test_update_total_percentage_once(self):

        action = self.actions[0][0]

        action.current_unit = 2
        action.goal_unit = 10
        action.period = Period.ONCE
        total_period = timedelta(days=10)

        self.board.start_at = datetime.today()
        self.board.end_at = self.board.start_at + total_period
        self.board.update_total_percentage(action)
        self.assertEqual(self.board.total_percentage, 2)

    def test_update_total_percentage_weekly(self):

        action = self.actions[0][0]

        action.current_unit = 2
        action.goal_unit = 10
        action.period = Period.WEEKLY
        total_period = timedelta(days=10)

        self.board.start_at = datetime.today()
        self.board.end_at = self.board.start_at + total_period
        self.board.update_total_percentage(action)
        self.assertEqual(self.board.total_percentage, 14)

    def test_update_total_percentage_monthly(self):
        action = self.actions[0][0]

        action.current_unit = 2
        action.goal_unit = 10
        action.period = Period.MONTHLY
        total_period = timedelta(days=10)

        self.board.start_at = datetime.today()
        self.board.end_at = self.board.start_at + total_period
        self.board.update_total_percentage(action)
        self.assertEqual(self.board.total_percentage, 60)

    def test_update_total_percentage_yearly(self):
        action = self.actions[0][0]

        action.current_unit = 2
        action.goal_unit = 10
        action.period = Period.YEARLY
        total_period = timedelta(days=10)

        self.board.start_at = datetime.today()
        self.board.end_at = self.board.start_at + total_period
        self.board.update_total_percentage(action)
        self.assertEqual(self.board.total_percentage, 730)
