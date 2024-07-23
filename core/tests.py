import typing

from rest_framework.test import APITestCase

from core.factories import AccountFactory

if typing:
    from apps.auth.models import Account


# Create your tests here.
class BaseAPITestCase(APITestCase):
    def get_authenticated_user(self, user=None) -> "Account":
        if not user:
            user = AccountFactory()
        self.client.force_authenticate(user=user)
        return user
