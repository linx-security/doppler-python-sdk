import unittest
from src.dopplersdk.models.ListResponse import ListResponse


class TestListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_list_response(self):
        # Create ListResponse class instance
        test_model = ListResponse(page=7, projects=["harum", "est"])
        self.assertEqual(test_model.page, 7)
        self.assertEqual(test_model.projects, ["harum", "est"])


if __name__ == "__main__":
    unittest.main()
