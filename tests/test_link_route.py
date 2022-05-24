import unittest
import json

from tests.BaseCase import BaseCase

class TestLinkRoute(BaseCase):

    def test_empty_response(self):
        response = self.app.get('/api/link')
        self.assertListEqual(response.json, [])
        self.assertEqual(response.status_code, 200)

    def test_links_post_response(self):
        # Given
        link_payload = {
            "url": "google.com",
        }

        # When
        response = self.app.post('/api/link',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))
        link_id = response.json['id']

        # Then
        self.assertIsNotNone(link_id)
        self.assertEqual(200, response.status_code)

    def test_links_response(self):
        # Given
        link_payload = {
            "url": "google.com",
        }
        response = self.app.post('/api/link',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))

        # When
        response = self.app.get('/api/link')
        added_link = response.json[0]

        # Then
        self.assertEqual(link_payload['url'], added_link['url'])
        self.assertEqual(200, response.status_code)

    def test_unique_link_response(self):
        # Given
        link_payload = {
            "url": "google.com",
        }
        response = self.app.post('/api/link',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))

        #Get the mongo id
        link_id = response.json['id']

        # When
        response = self.app.get(f'/api/link/{ link_id }')
        added_link = response.json

        # Then
        self.assertEqual(link_payload['url'], added_link['url'])
        self.assertEqual(200, response.status_code)

    def test_link_modify_response(self):
        # Given
        link_payload = {
            "url": "google.com",
        }

        second_payload = {
            "url": "yahoo.com",
            "short_url": "1234"
        }

        response = self.app.post('/api/link',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))

        link_id = response.json['id']
        response = self.app.get(f'/api/link/{link_id}')
        added_link = response.json

        # When
        response = self.app.put(f'/api/link/{link_id}',
            headers={"Content-Type": "application/json"},
            data=json.dumps(second_payload))
        
        self.assertEqual(200, response.status_code)

        response = self.app.get(f'/api/link/{link_id}')
        added_link = response.json

        # Then
        self.assertEqual(second_payload['url'], added_link['url'])
        self.assertEqual(second_payload['short_url'], added_link['short_url'])
        self.assertEqual(200, response.status_code)

    def test_link_delete_response(self):
        # Given
        link_payload = {
            "url": "google.com",
        }
        response = self.app.post('/api/link',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))

        #Get the mongo id
        link_id = response.json['id']

        # When
        response = self.app.delete(f'/api/link/{ link_id }')

        # Then
        self.assertEqual(200, response.status_code)