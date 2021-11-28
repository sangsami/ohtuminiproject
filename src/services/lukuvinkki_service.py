from entities.lukuvinkki import Lukuvinkki
from repositories.lukuvinkki_repository import lukuvinkki_repository as default_lukuvinkki_repository

class LukuvinkkiExistsError(Exception):
    pass

class LukuvinkkiTitleOrAuthor(Exception):
    pass

class LukuvinkkiService:
    def __init__(self, lukuvinkki_repository=default_lukuvinkki_repository):
        self._lukuvinkki_repository = lukuvinkki_repository

    def create_lukuvinkki(self, title, author, description, link, comment):
        if len(title) == 0 or len(author) == 0:
            raise LukuvinkkiTitleOrAuthor("Check that you have entered atleast a title and an author.")
        if self._lukuvinkki_repository.check_lukuvinkki(title, author):
            raise LukuvinkkiExistsError("The lukuvinkki already exists.")
        self._lukuvinkki_repository.create(Lukuvinkki(title, author, description, link, comment))
    
    def get_lukuvinkkis(self):
        return self._lukuvinkki_repository.find_all()

lukuvinkki_service = LukuvinkkiService()