import unittest
from entities.lukuvinkki import Lukuvinkki


class TestLukuvinkkiClass(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_lukuvinkki_prints_correctily(self):
        test_title = "test_title"
        test_author = "test_author"
        lukuvinkki = Lukuvinkki(test_title, test_author, "", "", "")

        self.assertEqual(f"{test_title} {test_author}", str(lukuvinkki))
