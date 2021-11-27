from entities.lukuvinkki import Lukuvinkki
from repositories.lukuvinkki_repository import lukuvinkki_repository as default_lukuvinkki_repository

class LukuvinkkiService:
    def __init__(self, lukuvinkki_repository=default_lukuvinkki_repository):
        self._lukuvinkki_repository = lukuvinkki_repository

    def create_lukuvinkki(self, title, author, description, link, comment):
        #should it check if the same title/author-combination exists from before?
        self._lukuvinkki_repository.create(Lukuvinkki(title, author, description, link, comment))
    
    def get_lukuvinkkis():
        return self._lukuvinkki_repository.get_lukuvinkkis()