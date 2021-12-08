import unittest
from unittest.mock import Mock
from models.user import User
from repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.db_mock = Mock()

        self.results = [
            User('matti', 'sha256asdasd'),
            User('testaaja', 'sha256qwerty')
        ]

        self.db_mock.session.query().all.return_value = self.results


        self.user_mock = Mock()
        self.user_repository = UserRepository(self.db_mock, self.user_mock)

    def test_db_find_users(self):
        result = self.user_repository.find_users()

        self.assertAlmostEqual(result, self.results)

    def test_db_find_user_by_username(self):
        self.db_mock.session.query().filter_by().first.return_value = self.results[1]
        result = self.user_repository.find_by_username('testaaja')
        self.assertAlmostEqual(result.username, 'testaaja')

    def test_db_find_user_by_non_existing_username(self):
        self.db_mock.session.query().filter_by().first.return_value = None
        result = self.user_repository.find_by_username('eiOlemassa')
        self.assertIsNone(result)

    def test_create_user(self):
        self.db_mock.session.query().filter_by().first.return_value = None
        self.user_repository.create(self.user_mock)

        self.db_mock.session.add.assert_called()
        self.db_mock.session.commit.assert_called()

    def test_create_user_existing_name(self):
        self.db_mock.session.query().filter_by().first.return_value = self.results[1]
        self.user_repository.create(self.user_mock)

        self.db_mock.session.add.assert_not_called()
        self.db_mock.session.commit.assert_not_called()
