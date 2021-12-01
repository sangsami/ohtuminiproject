import unittest
from entities.lukuvinkki import Lukuvinkki


class TestLukuvinkkiClass(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_lukuvinkki_returns_correct_title(self):
        test_title = "test_title"
        lukuvinkki = Lukuvinkki("test_title", "", "", "", "")

        self.assertEqual(test_title, lukuvinkki.title())

    def test_lukuvinkki_returns_correct_author(self):
        test_author = "test_author"
        lukuvinkki = Lukuvinkki("", test_author, "", "", "")

        self.assertEqual(test_author, lukuvinkki.author())

    def test_lukuvinkki_returns_correct_description(self):
        test_description = "test_description"
        lukuvinkki = Lukuvinkki("", "", test_description, "", "")

        self.assertEqual(test_description, lukuvinkki.description())

    def test_lukuvinkki_returns_correct_link(self):
        test_link = "test_link"
        lukuvinkki = Lukuvinkki("", "", "", test_link, "")

        self.assertEqual(test_link, lukuvinkki.link())

    def test_lukuvinkki_returns_correct_comment(self):
        test_comment = "test_comment"
        lukuvinkki = Lukuvinkki("", "", "", "", test_comment)

        self.assertEqual(test_comment, lukuvinkki.comment())

    def test_lukuvinkki_prints_correctily(self):
        test_title = "test_title"
        test_author = "test_author"
        lukuvinkki = Lukuvinkki(test_title, test_author, "", "", "")

        self.assertEqual(f"{test_title} {test_author}", str(lukuvinkki))
