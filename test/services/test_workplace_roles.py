import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.workplace_roles import WorkplaceRoles


class TestWorkplaceRoles_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/workplace/roles", json={}, status=200)
        # call the method to test
        test_service = WorkplaceRoles("testkey")
        response = test_service.list()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/workplace/roles", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = WorkplaceRoles("testkey")
            test_service.list()
        responses.reset()

    @responses.activate
    def test_create(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/roles", json={}, status=200
        )
        # call the method to test
        test_service = WorkplaceRoles("testkey")
        response = test_service.create()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/roles", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = WorkplaceRoles("testkey")
            test_service.create()
        responses.reset()

    @responses.activate
    def test_list_permissions(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/permissions", json={}, status=200
        )
        # call the method to test
        test_service = WorkplaceRoles("testkey")
        response = test_service.list_permissions()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_permissions_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/permissions", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = WorkplaceRoles("testkey")
            test_service.list_permissions()
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/roles/role/ipsum", json={}, status=200
        )
        # call the method to test
        test_service = WorkplaceRoles("testkey")
        response = test_service.get("ipsum")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/roles/role/quaerat",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = WorkplaceRoles("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/roles/role/facilis",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = WorkplaceRoles("testkey")
            test_service.get("facilis")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/roles/role/iste", json={}, status=200
        )
        # call the method to test
        test_service = WorkplaceRoles("testkey")
        response = test_service.update("iste")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/roles/role/architecto",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = WorkplaceRoles("testkey")
            test_service.update()
        responses.reset(),

    @responses.activate
    def test_update_error_on_non_200(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/roles/role/quibusdam",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = WorkplaceRoles("testkey")
            test_service.update("quibusdam")
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/roles/role/fuga", json={}, status=200
        )
        # call the method to test
        test_service = WorkplaceRoles("testkey")
        response = test_service.delete("fuga")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/roles/role/dolores",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = WorkplaceRoles("testkey")
            test_service.delete()
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/roles/role/ipsum", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = WorkplaceRoles("testkey")
            test_service.delete("ipsum")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
