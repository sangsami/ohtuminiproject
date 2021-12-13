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
                        )

    def test_repository_creates_lukuvinkkis(self):
        self.lukuvinkki_repository.create(self.lukuvinkki)
        testvinkkis = self.lukuvinkki_repository.find_all()
        title = testvinkkis[0].title
        author = testvinkkis[0].author
        isbn = testvinkkis[0].isbn
        descript = testvinkkis[0].descript
        link = testvinkkis[0].link
        comment = testvinkkis[0].comment
        self.lukuvinkki_repository.delete_lukuvinkki(testvinkkis[0].lukuvinkki_id)
        self.assertEqual(title, "A title")
        self.assertEqual(author, "An author")
        self.assertEqual(isbn, "isbn")
        self.assertEqual(descript, "A description")
        self.assertEqual(link, "A link")
        self.assertEqual(comment, "A comment")

    def test_repository_checks_lukuvinkki_that_exists(self):
        self.lukuvinkki_repository.create(self.lukuvinkki)
        testvinkkis = self.lukuvinkki_repository.find_all()
        flag = self.lukuvinkki_repository.check_lukuvinkki("A title")
        self.lukuvinkki_repository.delete_lukuvinkki(testvinkkis[0].lukuvinkki_id)
        self.assertTrue(flag)

    def test_repository_checks_lukuvinkki_that_does_not_exist(self):
        flag = self.lukuvinkki_repository.check_lukuvinkki("A title that probably does not exit because the name is super long and obscure vol.2")
        self.assertFalse(flag)

    def test_repository_checks_lukuvinkki_that_does_not_exists(self):
        self.lukuvinkki_repository.create(self.lukuvinkki)
        testvinkkis = self.lukuvinkki_repository.find_all()
        title = testvinkkis[0].title
        author = testvinkkis[0].author
        isbn = testvinkkis[0].isbn
        descript = testvinkkis[0].descript
        link = testvinkkis[0].link
        comment = testvinkkis[0].comment
        self.lukuvinkki_repository.delete_lukuvinkki(testvinkkis[0].lukuvinkki_id)
        self.assertEqual(title, "A title")
        self.assertEqual(author, "An author")
        self.assertEqual(isbn, "isbn")
        self.assertEqual(descript, "A description")
        self.assertEqual(link, "A link")
        self.assertEqual(comment, "A comment")
