from entities.lukuvinkki import Lukuvinkki

class LukuvinkkiRepository:
    def __init__(self):
        self._lukuvinkkis = []

    def find_all(self):
        return self._lukuvinkkis

    def create(self, lukuvinkki):
        self._lukuvinkkis.append(lukuvinkki)

lukuvinkki_repository = LukuvinkkiRepository()
