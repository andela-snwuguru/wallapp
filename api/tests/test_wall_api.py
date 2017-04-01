import json
from rest_framework.test import APITestCase
from api.tests.test_auth_api import register, login, decode_json


class WallApiTest(APITestCase):

    def setUp(self):
        register(self.client)
        self.login_response = decode_json(login(self.client))

    def create(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.login_response.get('token'))
        data = {
            'message': 'abc'
        }
        return self.client.post('/api/walls/', data=data)

    def test_wall_create(self):
        response = self.create()
        self.assertEqual(response.status_code, 201)

    def test_wall_create_without_token(self):
        data = {
            'message': 'abc'
        }
        response = self.client.post('/api/walls/', data=data)
        self.assertEqual(response.status_code, 401)

    def test_list_walls(self):
        self.create()
        response = self.client.get('/api/walls/')
        result = decode_json(response)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get('message'), 'abc')
