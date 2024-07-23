from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from apps.auth.factories import AccountFactory


# Create your tests here.
class TestAuth(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.account = AccountFactory()

    def test_signup_duplicated_email(self):
        url = reverse("rest_register")
        response = self.client.post(
            path=url,
            data={
                "username": "test0",
                "email": "test0@example.com",
                "password1": "test1234!",
                "password2": "test1234!",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
