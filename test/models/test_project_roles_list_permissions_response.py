import unittest
from src.dopplersdk.models.ProjectRolesListPermissionsResponse import (
    ProjectRolesListPermissionsResponse,
)


class TestProjectRolesListPermissionsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_project_roles_list_permissions_response(self):
        # Create ProjectRolesListPermissionsResponse class instance
        test_model = ProjectRolesListPermissionsResponse(permissions=["cum", "quae"])
        self.assertEqual(test_model.permissions, ["cum", "quae"])


if __name__ == "__main__":
    unittest.main()
