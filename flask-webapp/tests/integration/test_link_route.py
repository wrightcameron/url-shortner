import json

from tests.integration.BaseCase import BaseCase


class TestLinkRoute(BaseCase):

    def test_empty_response(self):
        """A 200 response should be returned when calling route /api/link
        """
        response = self.app.get('/api/link')
        self.assertListEqual(response.json, [])
        self.assertEqual(response.status_code, 200)

    def test_links_post_response(self):
        """Test /api/link post request, check if url is successfully added
        """
        # Given
        link_payload = {
            "url": "https://google.com",
        }

        # When
        response = self.app.post(
            '/api/link',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))
        link_id = response.json['id']

        # Then
        self.assertIsNotNone(link_id)
        self.assertEqual(200, response.status_code)

    def test_links_missing_http(self):
        """If a http(s) is not passed in, chech that it is added so the
           redirect route works.
        """
        # Given
        link_payload = {
            "url": "google.com",
        }
        # When
        response = self.app.post(
            '/api/link',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))
        link_id = response.json['id']
        # Get entry added
        response = self.app.get(f'/api/link/{ link_id }')
        added_link = response.json

        # Then
        self.assertIn('https://', added_link['url'])
        self.assertEqual(200, response.status_code)

    def test_links_response(self):
        """Test that /api/link can return 1:M responses
            (it should return all links stored)
        """
        # Given
        link_payload = {
            "url": "https://google.com",
        }
        response = self.app.post(
            '/api/link',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))

        # When
        response = self.app.get('/api/link')
        added_link = response.json[0]

        # Then
        self.assertEqual(link_payload['url'], added_link['url'])
        self.assertEqual(200, response.status_code)

    def test_unique_link_response(self):
        """Test /api/link/<id> route and check if it returns the unique url
        """
        # Given
        link_payload = {
            "url": "https://google.com",
        }
        response = self.app.post(
            '/api/link',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))

        # Get the mongo id
        link_id = response.json['id']

        # When
        response = self.app.get(f'/api/link/{ link_id }')
        added_link = response.json

        # Then
        self.assertEqual(link_payload['url'], added_link['url'])
        self.assertEqual(200, response.status_code)

    def test_random_response(self):
        """Test the /api/link/random route, check that it returns a url
        """
        # Given
        link_payload = {
            "url": "https://google.com",
        }
        response = self.app.post(
            '/api/link',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))

        # When
        response = self.app.get('/api/link/random')
        added_link = response.json

        # Then
        self.assertEqual(link_payload['url'], added_link['url'])
        self.assertEqual(200, response.status_code)

    def test_link_modify_response(self):
        """Test that the /api/link/<id> route with PUT request can modify an entry.
        """
        # Given
        link_payload = {
            "url": "https://google.com",
        }

        second_payload = {
            "url": "https://yahoo.com",
            "short_url": "1234"
        }

        response = self.app.post(
            '/api/link',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))

        link_id = response.json['id']
        response = self.app.get(f'/api/link/{link_id}')
        added_link = response.json

        # When
        response = self.app.put(
            f'/api/link/{link_id}',
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
        """Test /api/link/<id> route can delete an entry
        """
        # Given
        link_payload = {
            "url": "https://google.com",
        }
        response = self.app.post(
            '/api/link',
            headers={"Content-Type": "application/json"},
            data=json.dumps(link_payload))

        # Get the mongo id
        link_id = response.json['id']

        # When
        response = self.app.delete(f'/api/link/{ link_id }')

        # Then
        self.assertEqual(200, response.status_code)
