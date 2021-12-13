import unittest
from app import db
from models.user import User

class TestUserModel(unittest.TestCase):
    def setUp(self) -> None:
        self.user = db.session.query(User).filter_by(username='guest').first()


    def test_user_has_id(self):
        self.assertIsNotNone(self.user.id)

    def test_user_has_username(self):
        self.assertEqual(self.user.username, 'guest')

    def test_user_has_password_and_its_hashed(self):
        self.assertIsNotNone(self.user.password)
        self.assertNotEqual(self.user.password, 'veryStrongPassword')

    def test_user_has_time_created(self):
        self.assertIsNotNone(self.user.time_created)

    def test_user_is_printed_correctly(self):
        self.assertAlmostEqual(
            str(self.user),
            f'<User(username=guest, time_created={self.user.time_created})>'
            )
