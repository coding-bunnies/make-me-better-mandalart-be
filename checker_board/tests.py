from django.urls import reverse
from rest_framework import status

from auth.factories import AccountFactory
from checker_board.factories import BoardFactory, MissionFactory
from core.tests import BaseAPITestCase


# Create your tests here.
class BoardViewTest(BaseAPITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = AccountFactory()
        cls.board = BoardFactory(user=cls.user)
        cls.list_url = reverse("board-list")
        cls.detail_url = reverse("board-detail", args=[cls.board.id])

    def test_get_list(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_unauthenticated(self):
        response = self.client.get(self.list_url)
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


class MissionViewTest(BaseAPITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = AccountFactory()
        cls.board = BoardFactory(user=cls.user)
        cls.mission = MissionFactory(board=cls.board)
        cls.list_url = reverse("mission-list")
        cls.detail_url = reverse("mission-detail", args=[cls.mission.id])

    def test_get_list(self):
        self.get_authenticated_user(user=self.user)

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_unauthenticated(self):
        response = self.client.get(self.list_url)
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
