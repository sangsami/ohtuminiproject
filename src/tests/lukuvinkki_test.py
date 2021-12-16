import unittest
from app import db # pylint: disable=unused-import
from entities.lukuvinkki import Lukuvinkki

class TestLukuvinkkiClass(unittest.TestCase):
    def setUp(self) -> None:
        self.lukuvinkki_default_values = Lukuvinkki(
            "A title",
            "An author",
            "isbn",
            "A description",
            "A link",
            "A comment",
            1
            )

        self.lukuvinkki_has_type = Lukuvinkki(
            "A title",
            "An author",
            "isbn",
            "A description",
            "A link",
            "A comment",
            1,
            lukuvinkki_type="Podcast"
            )

        self.lukuvinkki_is_read = Lukuvinkki(
            "A title",
            "An author",
            "isbn",
            "A description",
            "A link",
            "A comment",
            1,
            is_read=True
            )

    def test_lukuvinkki_returns_right_status(self):
        self.assertEqual("Not read", self.lukuvinkki_default_values.read_status())

    def test_lukuvinkki_changes_status(self):
        self.lukuvinkki_default_values.change_read()
        self.assertTrue(self.lukuvinkki_default_values.is_read)

    def test_lukuvinkki_prints_correctly(self):
        self.assertEqual("Book: A title", str(self.lukuvinkki_default_values))
