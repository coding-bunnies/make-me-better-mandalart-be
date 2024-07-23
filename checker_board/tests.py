from django.urls import reverse
from rest_framework import status

from auth.factories import AccountFactory
from checker_board.factories import BoardFactory, MissionFactory, ActionFactory
from checker_board.models import Cycle
from core.const import DEFAULT_MISSION_COUNT
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
            "cycle": Cycle.ONCE,
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
                "cycle": Cycle.ONCE,
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
