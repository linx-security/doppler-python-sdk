import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.service_accounts import ServiceAccounts


class TestServiceAccounts_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/service_accounts", json={}, status=200
        )
        # call the method to test
        test_service = ServiceAccounts("testkey")
        response = test_service.list(3, 5)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/service_accounts", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = ServiceAccounts("testkey")
            test_service.list(8, 8)
        responses.reset()

    @responses.activate
    def test_create(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/service_accounts", json={}, status=200
        )
        # call the method to test
        test_service = ServiceAccounts("testkey")
        response = test_service.create({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/service_accounts", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = ServiceAccounts("testkey")
            test_service.create({})
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/quidem",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ServiceAccounts("testkey")
        response = test_service.get("quidem")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/et",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = ServiceAccounts("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/quod",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ServiceAccounts("testkey")
            test_service.get("quod")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/magni",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ServiceAccounts("testkey")
        response = test_service.update("magni", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/sequi",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = ServiceAccounts("testkey")
            test_service.update()
        responses.reset(),

    @responses.activate
    def test_update_error_on_non_200(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/quis",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ServiceAccounts("testkey")
            test_service.update("quis", {})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/animi",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ServiceAccounts("testkey")
        response = test_service.delete("animi")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/eius",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = ServiceAccounts("testkey")
            test_service.delete()
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/assumenda",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ServiceAccounts("testkey")
            test_service.delete("assumenda")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
