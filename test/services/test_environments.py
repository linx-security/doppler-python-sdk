import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.environments import Environments


class TestEnvironments_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/environments/environment", json={}, status=200
        )
        # call the method to test
        test_service = Environments("testkey")
        response = test_service.get("occaecati", "sequi")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/environments/environment", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Environments("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/environments/environment", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Environments("testkey")
            test_service.get("nostrum", "natus")
        responses.reset()

    @responses.activate
    def test_rename(self):
        # Mock the API response
        responses.put(
            "https://api.doppler.com/v3/environments/environment", json={}, status=200
        )
        # call the method to test
        test_service = Environments("testkey")
        response = test_service.rename("tenetur", "odit", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_rename_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "https://api.doppler.com/v3/environments/environment", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Environments("testkey")
            test_service.rename()
        responses.reset(),

    @responses.activate
    def test_rename_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "https://api.doppler.com/v3/environments/environment", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Environments("testkey")
            test_service.rename("quod", "aspernatur", {})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/environments/environment", json={}, status=200
        )
        # call the method to test
        test_service = Environments("testkey")
        response = test_service.delete("necessitatibus", "officiis")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/environments/environment", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Environments("testkey")
            test_service.delete()
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/environments/environment", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Environments("testkey")
            test_service.delete("fuga", "ab")
        responses.reset()

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/environments", json={}, status=200)
        # call the method to test
        test_service = Environments("testkey")
        response = test_service.list("quae")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_required_fields_missing(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/environments", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Environments("testkey")
            test_service.list()
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/environments", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Environments("testkey")
            test_service.list("dolorum")
        responses.reset()

    @responses.activate
    def test_create(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/environments", json={}, status=200)
        # call the method to test
        test_service = Environments("testkey")
        response = test_service.create("beatae", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_required_fields_missing(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/environments", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Environments("testkey")
            test_service.create()
        responses.reset(),

    @responses.activate
    def test_create_error_on_non_200(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/environments", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Environments("testkey")
            test_service.create("amet", {})
        responses.reset()


if __name__ == "__main__":
    unittest.main()
