import unittest
from unittest.mock import patch
from app import app
class TestShuffleEndpoint(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_shuffle_endpoint(self):
        response = self.client.get('/shuffle')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data["deck"]), 52)
        self.assertIn("Jack of Clubs", data["deck"])
