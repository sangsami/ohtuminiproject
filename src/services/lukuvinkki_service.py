from app import db
from entities.lukuvinkki import Lukuvinkki
from repositories.lukuvinkki_repository import (
    lukuvinkki_repository as default_lukuvinkki_repository
    )


class LukuvinkkiExistsError(Exception):
    pass


class LukuvinkkiTitle(Exception):
    pass

# pylint: disable=too-many-arguments
class LukuvinkkiService:
    def __init__(self, lukuvinkki_repository=default_lukuvinkki_repository):
        self._lukuvinkki_repository = lukuvinkki_repository

    def create_lukuvinkki(
            self, title, author, isbn, link, description, comment, lukuvinkki_type):
        if len(title) == 0:
            raise LukuvinkkiTitle(
                "Check that you have entered atleast a title.")
        if self._lukuvinkki_repository.check_lukuvinkki(title):
            raise LukuvinkkiExistsError("The lukuvinkki already exists.")
        self._lukuvinkki_repository.create(Lukuvinkki(
            title,
            author,
            isbn,
            link,
            description,
            comment,
            lukuvinkki_type
            ))

    def change_lukuvinkki(
            self,
            lukuvinkki_id,
            title,
            author,
            isbn,
            link,
            description,
            comment,
            lukuvinkki_type
            ):
        self._lukuvinkki_repository.change_lukuvinkki(
            lukuvinkki_id,
            title,
            author,
            isbn,
            link,
            description,
            comment,
            lukuvinkki_type)

    def change_lukuvinkki_status(self, lukuvinkki_id):
        lukuvinkki = self._lukuvinkki_repository.get_lukuvinkki(lukuvinkki_id)
        lukuvinkki.change_read()
        db.session.commit()

    def get_lukuvinkkis(self):
        return self._lukuvinkki_repository.find_all()

    def get_books(self):
        return self._lukuvinkki_repository.get_books()

    def get_blog_posts(self):
        return self._lukuvinkki_repository.get_blog_posts()

    def get_podcasts(self):
        return self._lukuvinkki_repository.get_podcasts()

    def get_youtubes(self):
        return self._lukuvinkki_repository.get_youtubes()

    def find_by_name(self, searchterm):
        return self._lukuvinkki_repository.find_by_name(searchterm)


lukuvinkki_service = LukuvinkkiService()
