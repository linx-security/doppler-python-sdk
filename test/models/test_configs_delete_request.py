import unittest
from src.dopplersdk.models.ConfigsDeleteRequest import ConfigsDeleteRequest


class TestConfigsDeleteRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_delete_request(self):
        # Create ConfigsDeleteRequest class instance
        test_model = ConfigsDeleteRequest(config="aliquid", project="molestiae")
        self.assertEqual(test_model.config, "aliquid")
        self.assertEqual(test_model.project, "molestiae")

    def test_configs_delete_request_required_fields_missing(self):
        # Assert ConfigsDeleteRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ConfigsDeleteRequest()


if __name__ == "__main__":
    unittest.main()
