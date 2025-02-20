import unittest
from src.dopplersdk.models.SyncsGetResponse import SyncsGetResponse


class TestSyncsGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_syncs_get_response(self):
        # Create SyncsGetResponse class instance
        test_model = SyncsGetResponse(sync={"ducimus": 9})
        self.assertEqual(test_model.sync, {"ducimus": 9})


if __name__ == "__main__":
    unittest.main()
