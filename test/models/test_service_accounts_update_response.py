import unittest
from src.dopplersdk.models.ServiceAccountsUpdateResponse import (
    ServiceAccountsUpdateResponse,
)


class TestServiceAccountsUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_accounts_update_response(self):
        # Create ServiceAccountsUpdateResponse class instance
        test_model = ServiceAccountsUpdateResponse(service_account={"laborum": 2})
        self.assertEqual(test_model.service_account, {"laborum": 2})


if __name__ == "__main__":
    unittest.main()
