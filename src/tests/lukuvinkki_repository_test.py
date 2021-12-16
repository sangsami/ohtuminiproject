import unittest
# pylint: disable=unused-import, disable=line-too-long
from app import db
from entities.lukuvinkki import Lukuvinkki
from repositories.lukuvinkki_repository import LukuvinkkiRepository


class TestLukuvinkkiRepository(unittest.TestCase):
    def setUp(self):
        self.lukuvinkki_repository = LukuvinkkiRepository()
        self.lukuvinkki = Lukuvinkki(
                        "A title",
                        "An author",
                        "isbn",
                        "A link",
                        "A description",
                        "A comment",
                        1,
                        is_read=False
                        )
        self.lukuvinkki_repository.create(self.lukuvinkki)

    def test_repository_creates_lukuvinkki(self):
        testvinkkis = self.lukuvinkki_repository.find_all()
        lukuvinkki_id = testvinkkis[0].lukuvinkki_id
        lukuvinkki = self.lukuvinkki_repository.get_lukuvinkki(lukuvinkki_id)
        title = lukuvinkki.title
        author = lukuvinkki.author
        isbn = lukuvinkki.isbn
        descript = lukuvinkki.descript
        link = lukuvinkki.link
        comment = lukuvinkki.comment
        self.assertEqual(title, "A title")
        self.assertEqual(author, "An author")
        self.assertEqual(isbn, "isbn")
        self.assertEqual(descript, "A description")
        self.assertEqual(link, "A link")
        self.assertEqual(comment, "A comment")

    def test_repository_checks_lukuvinkki_that_exists(self):
        flag = self.lukuvinkki_repository.check_lukuvinkki("A title", 1, "Book")
        self.assertTrue(flag)

    def test_repository_checks_lukuvinkki_that_does_not_exist(self):
        flag = self.lukuvinkki_repository.check_lukuvinkki("A title that probably does not exit because the name is super long and obscure vol.2", -1, "Book")
        self.assertFalse(flag)

    def test_repository_checks_lukuvinkki_that_does_not_exists(self):
        testvinkkis = self.lukuvinkki_repository.find_all()
        title = testvinkkis[0].title
        author = testvinkkis[0].author
        isbn = testvinkkis[0].isbn
        descript = testvinkkis[0].descript
        link = testvinkkis[0].link
        comment = testvinkkis[0].comment
        self.assertEqual(title, "A title")
        self.assertEqual(author, "An author")
        self.assertEqual(isbn, "isbn")
        self.assertEqual(descript, "A description")
        self.assertEqual(link, "A link")
        self.assertEqual(comment, "A comment")

    def test_repository_changes_read_status(self):
        testvinkkis = self.lukuvinkki_repository.find_all()
        lukuvinkki_id = testvinkkis[0].lukuvinkki_id
        lukuvinkki = self.lukuvinkki_repository.get_lukuvinkki(lukuvinkki_id)
        self.lukuvinkki_repository.change_lukuvinkki(
            lukuvinkki_id,
            "New title",
            "New author",
            "New isbn",
            "New link",
            "New description",
            "New comment",
            lukuvinkki.is_public,
            lukuvinkki.lukuvinkki_type
        )
        lukuvinkki = self.lukuvinkki_repository.get_lukuvinkki(lukuvinkki_id)
        self.assertEqual(lukuvinkki.title, "New title")
        self.assertEqual(lukuvinkki.author, "New author")
        self.assertEqual(lukuvinkki.isbn, "New isbn")
        self.assertEqual(lukuvinkki.descript, "New description")
        self.assertEqual(lukuvinkki.link, "New link")
        self.assertEqual(lukuvinkki.comment, "New comment")

    def test_repository_changes_lukuvinkki(self):
        testvinkkis = self.lukuvinkki_repository.find_all()
        lukuvinkki_id = testvinkkis[0].lukuvinkki_id
        self.lukuvinkki_repository.change_lukuvinkki_status(lukuvinkki_id)
        lukuvinkki = self.lukuvinkki_repository.get_lukuvinkki(lukuvinkki_id)
        self.assertTrue(lukuvinkki.is_read)