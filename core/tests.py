from rest_framework.test import APITestCase

from core.factories import AccountFactory


# Create your tests here.
class BaseAPITestCase(APITestCase):
    def get_authenticated_user(self, user=None) -> "AccountFactory":
        if not user:
            user = AccountFactory()
        self.client.force_authenticate(user=user)
        return user
