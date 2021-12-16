import unittest
from unittest.mock import Mock
from app import db  # pylint: disable=unused-import
from services.lukuvinkki_service import LukuvinkkiService, LukuvinkkiTitle, LukuvinkkiExistsError


lukuvinkki_repo_mock = Mock()


def check_lukuvinkki(title, user_id, lukuvinkki_type):
    if title == "exists" and user_id == 99999 and lukuvinkki_type == "Book":
        return True
    return False


lukuvinkki_repo_mock.check_lukuvinkki.side_effect = check_lukuvinkki


class TestLukuvinkkiClass(unittest.TestCase):
    def setUp(self) -> None:
        self.lukuvinkki_service = LukuvinkkiService(lukuvinkki_repo_mock)

    def test_cant_create_lukuvinkki_without_title(self):
        self.assertRaises(
            LukuvinkkiTitle, self.lukuvinkki_service.create_lukuvinkki, "", "", "", "", "", "", "")

    def test_cant_create_lukuvinkki_with_same_title_as_earlier_used(self):
        self.assertRaises(
            LukuvinkkiExistsError, self.lukuvinkki_service.create_lukuvinkki, "exists", "", "", "", "", "", user_id=99999, lukuvinkki_type="Book")

    def test_creates_lukuvinkki_if_has_title_and_doesnt_exist(self):
        self.lukuvinkki_service.create_lukuvinkki(
            "New title", "diiba", "daaba", "diiba", "daaba", "diiba", "daaba", 99999)
        lukuvinkki_repo_mock.create.assert_called()

    def test_change_lukuvinkki_calls_repository(self):
        self.lukuvinkki_service.change_lukuvinkki(
            "New info", "diiba1", "daaba2", "diiba3", "daaba4", "diiba5", "daaba6", "diiba7", 99999)
        lukuvinkki_repo_mock.change_lukuvinkki.assert_called_with(
            "New info", "diiba1", "daaba2", "diiba3", "daaba4", "diiba5", "daaba6", "diiba7", 99999)

    def test_get_lukuvinkkis_gets_lukuvinkkis(self):
        self.lukuvinkki_service.get_lukuvinkkis()
        lukuvinkki_repo_mock.find_all.assert_called()

    def test_get_books_gets_books(self):
        self.lukuvinkki_service.get_books(1)
        lukuvinkki_repo_mock.get_books.assert_called()
