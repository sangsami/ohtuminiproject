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
            self,
            title,
            author,
            isbn,
            link,
            description,
            comment,
            user_id,
            is_public,
            lukuvinkki_type
            ):
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
            user_id,
            is_public,
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
            is_public,
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
            is_public,
            lukuvinkki_type)

    def change_lukuvinkki_status(self, lukuvinkki_id):
        self._lukuvinkki_repository.change_lukuvinkki_status(lukuvinkki_id)

    def get_lukuvinkkis(self):
        return self._lukuvinkki_repository.find_all()

    def get_books(self, user_id, searchterm=""):
        return self._lukuvinkki_repository.get_books(user_id, searchterm)

    def get_blog_posts(self, user_id, searchterm=""):
        return self._lukuvinkki_repository.get_blog_posts(user_id, searchterm)

    def get_podcasts(self, user_id, searchterm=""):
        return self._lukuvinkki_repository.get_podcasts(user_id, searchterm)

    def get_youtubes(self, user_id, searchterm=""):
        return self._lukuvinkki_repository.get_youtubes(user_id, searchterm)

    def find_by_name(self, user_id, searchterm):
        return self._lukuvinkki_repository.find_by_name(user_id, searchterm)


lukuvinkki_service = LukuvinkkiService()
