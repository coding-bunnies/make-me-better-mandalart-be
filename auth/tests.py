from rest_framework.test import APITestCase


# Create your tests here.
class AuthTestCase(APITestCase):
    def test_registration(self):
        data = {
            'username': 'test',
            'email': 'test@example.com',
            'password': 'test1234',
        }
        response = self.client.post('/auth/registration/', data)
        self.assertEqual(response.status_code, 201)
