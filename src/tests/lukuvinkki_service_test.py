import unittest
from services.lukuvinkki_service import LukuvinkkiService, LukuvinkkiExistsError, LukuvinkkiTitleOrAuthor
from repositories.lukuvinkki_repository import LukuvinkkiRepository

class TestLukuvinkki(unittest.TestCase):
    def setUp(self):
        self._lukuvinkki_repository = LukuvinkkiRepository()
        self._lukuvinkki_service = LukuvinkkiService(self._lukuvinkki_repository)

    def test_can_add_new_lukuvinkki(self):
        self._lukuvinkki_repository.delete_all()
        self._lukuvinkki_service.create_lukuvinkki("A title", "An Author", "A description", "A link", "A comment")
        lukuvinkkis = self._lukuvinkki_service.get_lukuvinkkis()
        self.assertEqual(len(lukuvinkkis), 1)

    def test_cant_add_same_lukuvinkki_twice(self):
        self._lukuvinkki_repository.delete_all()
        self._lukuvinkki_service.create_lukuvinkki("A title", "An Author", "A description", "A link", "A comment")
        self.assertRaises(LukuvinkkiExistsError, self._lukuvinkki_service.create_lukuvinkki, "A title", "An Author", "A description", "A link", "A comment")

    def test_can_add_different_lukuvinkkis(self):
        self._lukuvinkki_repository.delete_all()
        self._lukuvinkki_service.create_lukuvinkki("A title", "An Author", "A description", "A link", "A comment")
        self._lukuvinkki_service.create_lukuvinkki("Another title", "Another Author", "A description", "A link", "A comment")
        lukuvinkkis = self._lukuvinkki_service.get_lukuvinkkis()
        self.assertEqual(len(lukuvinkkis), 2)

    def test_cant_add_lukuvinkki_without_title(self):
        self.assertRaises(LukuvinkkiTitleOrAuthor, self._lukuvinkki_service.create_lukuvinkki, "", "", "", "", "")

    def test_cant_add_lukuvinkki_without_author(self):
        self.assertRaises(LukuvinkkiTitleOrAuthor, self._lukuvinkki_service.create_lukuvinkki, "A title", "", "", "", "")
    



