import unittest
from unittest.mock import Mock
from werkzeug.security import generate_password_hash
from app import db # pylint: disable=unused-import
from services.user_service import UserService
from models.user import User

class TestUserServiceClass(unittest.TestCase):
    def setUp(self) -> None:
        self.user_repo_mock = Mock()
        self.user_model_mock = Mock()

        self.user_repo_mock.find_by_username.side_effect = [
            None,
            User('username', generate_password_hash('password', method='sha256'))
            ]

        self.user_service = UserService(self.user_repo_mock, User)

    def test_check_credentials_looks_for_username(self):
        self.user_service.check_credentials('username', 'password')
        self.user_repo_mock.find_by_username.assert_called_with('username')

    def test_check_credentials_returns_none_if_not_user(self):
        result = self.user_service.check_credentials('username', 'password')
        self.assertIsNone(result)

    def test_check_credentials_returns_user_if_user_and_correct_password(self):
        self.user_service.check_credentials('username', 'password')
        result = self.user_service.check_credentials('username', 'password')
        self.assertIsNotNone(result)

    def test_create_user_creates_user(self):
        self.user_service.create_user("username", "password")
        self.user_repo_mock.create.assert_called()

    def test_create_user_is_called_with_username_and_password(self):
        self.user_service.create_user("username", "password")
        self.user_repo_mock.create.assert_called_with(User('username', 'password'))

    def test_get_user_calls_repo(self):
        self.user_service.get_user('user_id')
        self.user_repo_mock.find_by_id.assert_called_with('user_id')

    def test_check_if_unique_username_returns_false_if_not_unique(self):
        self.user_service.check_if_unique_username('username')
        self.assertFalse(self.user_service.check_if_unique_username('username'))

    def test_check_if_unique_username_returns_true_if_unique(self):
        self.assertTrue(self.user_service.check_if_unique_username('username'))
