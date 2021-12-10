import unittest
from unittest.mock import Mock, ANY
from app import db # pylint: disable=unused-import
from services.lukuvinkki_service import LukuvinkkiService, LukuvinkkiTitle, LukuvinkkiExistsError

class Lukuvinkki_repo_stub:
    def __init__(self):
        pass
    
    def check_lukuvinkki(self, title):
        if title=="exists":
            return True
        return False

lukuvinkki_repo_mock = Mock()

def check_lukuvinkki(title):
    if title=="exists":
        return True
    return False

lukuvinkki_repo_mock.check_lukuvinkki.side_effect = check_lukuvinkki

class TestLukuvinkkiClass(unittest.TestCase):
    def setUp(self) -> None:
        self.lukuvinkki_service = LukuvinkkiService(lukuvinkki_repo_mock)

    def test_cant_create_lukuvinkki_without_title(self):
        self.assertRaises(LukuvinkkiTitle, self.lukuvinkki_service.create_lukuvinkki, "", "", "", "", "", "", "")

    def test_cant_create_lukuvinkki_with_same_title_as_earlier_used(self):
        self.assertRaises(LukuvinkkiExistsError, self.lukuvinkki_service.create_lukuvinkki, "exists", "", "", "", "", "", "")

    def test_creates_lukuvinkki_if_has_title_and_doesnt_exist(self):
        self.lukuvinkki_service.create_lukuvinkki("New title", "diiba", "daaba", "diiba", "daaba", "diiba", "daaba")
        lukuvinkki_repo_mock.create.assert_called()

    def test_change_lukuvinkki_calls_repository(self):
        self.lukuvinkki_service.change_lukuvinkki("New info", "diiba1", "daaba2", "diiba3", "daaba4", "diiba5", "daaba6", "diiba7")
        lukuvinkki_repo_mock.change_lukuvinkki.assert_called_with("New info", "diiba1", "daaba2", "diiba3", "daaba4", "diiba5", "daaba6", "diiba7")