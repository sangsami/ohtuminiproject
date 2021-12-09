from entities.lukuvinkki import Lukuvinkki  # pylint: disable=unused-import
from app import db

class LukuvinkkiRepository:
    def __init__(self):
        self._lukuvinkkis = []

    def get_books(self):
        return Lukuvinkki.query.filter(Lukuvinkki.current_type=="Book").order_by(Lukuvinkki.id.desc()).all()

    def get_blog_posts(self):
        return Lukuvinkki.query.filter(Lukuvinkki.current_type=="Blog post").order_by(Lukuvinkki.id.desc()).all()

    def get_podcasts(self):
        return Lukuvinkki.query.filter(Lukuvinkki.current_type=="Podcast").order_by(Lukuvinkki.id.desc()).all()

    def get_youtubes(self):
        return Lukuvinkki.query.filter(Lukuvinkki.current_type=="Youtube").order_by(Lukuvinkki.id.desc()).all()

    def find_all(self):
        return Lukuvinkki.query.order_by(Lukuvinkki.id.desc()).all()

    def create(self, lukuvinkki):
        db.session.add(lukuvinkki)
        db.session.commit()

    def change_lukuvinkki(self, id, title, author, link, description, comment, type):
        lukuvinkki = self.get_lukuvinkki(id)
        lukuvinkki.title = title,
        lukuvinkki.author = author,
        lukuvinkki.link = link,
        lukuvinkki.descript = description,
        lukuvinkki.comment = comment,
        lukuvinkki.type = type,
        db.session.commit()

    def check_lukuvinkki(self, title):
        for lukuvinkki in self._lukuvinkkis:
            if title == lukuvinkki.title:
                return True
        return False
    
    def get_lukuvinkki(self, id):
        return Lukuvinkki.query.get(id)

    def delete_all(self):
        self._lukuvinkkis = []

    def example_db_ops(self):
        sql = "INSERT into test (username, password) VALUES (:username, :password);"
        db.session.execute(sql, {"username": "demo", "password": "no-crypto"})
        db.session.commit()


lukuvinkki_repository = LukuvinkkiRepository()
