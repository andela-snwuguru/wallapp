import json
from rest_framework.test import APITestCase


def register(client):
    user_detail = {
        'username': 'tester',
        'first_name': 'tester',
        'last_name': 'tester',
        'email': 'test@example.com',
        'password': 'tester123',
    }
    return client.post('/api/register/', user_detail)


def login(client, username="tester", password="tester123"):
    user_detail = {
        'username': username,
        'password': password
    }
    return client.post('/api/login/', user_detail)


def decode_json(response):
    return json.loads(response.content)


class AccountTest(APITestCase):

    def setUp(self):
        self.register_response = register(self.client)

    def test_register(self):
        self.assertEqual(self.register_response.status_code, 201)

    def test_login(self):
        response = login(self.client)
        self.assertEqual(response.status_code, 200)
        result = decode_json(response)
        user_data = result.get('user')
        self.assertEqual(user_data.get('username') ,'tester')
        self.assertNotEqual(result.get('token'), '')

    def test_login_with_wrong_user(self):
        response = login(self.client, 'wrong user')
        expected = {
          "non_field_errors": [
            "Unable to log in with provided credentials."
          ]
        }
        result = decode_json(response)
        self.assertEqual(result, expected)
