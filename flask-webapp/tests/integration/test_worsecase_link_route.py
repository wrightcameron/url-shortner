import unittest
import json

from tests.integration.BaseCase import BaseCase

class TestLinkRoute(BaseCase):

    def test_links__get_incorrectid(self):
        """For /api/link/<id> GET what happens if the id doesn't exist/wrong
        """
        # Given
        id = 'wrong'

        # When
        response = self.app.get(f'/api/link/{id}',
            headers={"Content-Type": "application/json"})
        
        # Then
        self.assertEqual(400, response.status_code)
        self.assertEqual("Link with given id doesn't exist", response.json['message'])

    def test_links_put_incorrectid(self):
        """For /api/link/<id> PUT what happens if the id doesn't exist/wrong
        """
        # Given
        id = 'wrong'
        link_payload = {
            "url": "https://google.com",
        }

        # When
        response = self.app.put(f'/api/link/{id}',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))
        
        # Then
        self.assertEqual(400, response.status_code)
        self.assertEqual("Link with given id doesn't exist", response.json['message'])


    def test_links_delete_incorrectid(self):
        """For /api/link/<id> DELETE what happens if the id doesn't exist/wrong
        """
        # Given
        id = 'wrong'
        link_payload = {
            "url": "https://google.com",
        }

        # When
        response = self.app.delete(f'/api/link/{id}',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))
        
        # Then
        self.assertEqual(400, response.status_code)
        self.assertEqual("Link with given id doesn't exist", response.json['message'])

    def test_links_post_response(self):
        """Test /api/link post request, check if url is successfully added
        """
        # Given
        link_payload = {
            "url": "https://google.com",
        }

        # When
        response = self.app.post('/api/link',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))
        link_id = response.json['id']

        # Then
        self.assertIsNotNone(link_id)
        self.assertEqual(200, response.status_code)