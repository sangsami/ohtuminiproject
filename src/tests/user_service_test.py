import unittest
from unittest.mock import Mock, ANY
from app import db # pylint: disable=unused-import
from services.user_service import UserService



user_repo_mock = Mock()
user_model_mock = Mock()

def find_by_username(username):
    return None

user_repo_mock.find_by_username.side_effect = find_by_username

class TestUserServiceClass(unittest.TestCase):
    def setUp(self) -> None:
        self.user_service = UserService(user_repo_mock, user_model_mock)

    def test_check_credentials_looks_for_username(self):
        self.user_service.check_credentials('username', 'password')
        user_repo_mock.find_by_username.assert_called_with('username')

    def test_create_user_creates_user(self):
        self.user_service.create_user("username", "password")
        user_repo_mock.create.assert_called()
