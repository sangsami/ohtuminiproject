from entities.lukuvinkki import Lukuvinkki  # pylint: disable=unused-import
from app import db

# pylint: disable=line-too-long
class LukuvinkkiRepository:
    def __init__(self):
        pass

    def get_books(self, searchterm=""):
        return Lukuvinkki.query.filter(Lukuvinkki.lukuvinkki_type == "Book").filter(Lukuvinkki.title.ilike("%" + searchterm +"%")).order_by(Lukuvinkki.lukuvinkki_id.desc()).all()

    def get_blog_posts(self, searchterm=""):
        return Lukuvinkki.query.filter(Lukuvinkki.lukuvinkki_type == "Blog post").filter(Lukuvinkki.title.ilike("%" + searchterm +"%")).order_by(Lukuvinkki.lukuvinkki_id.desc()).all()

    def get_podcasts(self, searchterm=""):
        return Lukuvinkki.query.filter(Lukuvinkki.lukuvinkki_type == "Podcast").filter(Lukuvinkki.title.ilike("%" + searchterm +"%")).order_by(Lukuvinkki.lukuvinkki_id.desc()).all()

    def get_youtubes(self, searchterm=""):
        return Lukuvinkki.query.filter(Lukuvinkki.lukuvinkki_type == "Youtube").filter(Lukuvinkki.title.ilike("%" + searchterm +"%")).order_by(Lukuvinkki.lukuvinkki_id.desc()).all()

    def find_all(self):
        return Lukuvinkki.query.order_by(Lukuvinkki.lukuvinkki_id.desc()).all()

# pylint: enable=line-too-long, disable=too-many-arguments

    def create(self, lukuvinkki):
        db.session.add(lukuvinkki)
        db.session.commit()

    def change_lukuvinkki(
            self,
            lukuvinkki_id,
            title, author, isbn, link,
            description, comment,
            lukuvinkki_type
            ):
        lukuvinkki = self.get_lukuvinkki(lukuvinkki_id)
        lukuvinkki.title = title
        lukuvinkki.author = author
        lukuvinkki.isbn = isbn
        lukuvinkki.link = link
        lukuvinkki.descript = description
        lukuvinkki.comment = comment
        lukuvinkki.lukuvinkki_type = lukuvinkki_type
        db.session.commit()

# pylint: disable=line-too-long

    def check_lukuvinkki(self, title):
        query_title = Lukuvinkki.query.filter(Lukuvinkki.title == title).first()
        if query_title is not None:
            return True
        return False

    def get_lukuvinkki(self, lukuvinkki_id):
        return Lukuvinkki.query.get(lukuvinkki_id)

    def delete_lukuvinkki(self, lukuvinkki_id):
        record_obj = Lukuvinkki.query.filter(Lukuvinkki.lukuvinkki_id==lukuvinkki_id).first()
        db.session.delete(record_obj)
        db.session.commit()

    def example_db_ops(self):
        sql = "INSERT into test (username, password) VALUES (:username, :password);"
        db.session.execute(sql, {"username": "demo", "password": "no-crypto"})
        db.session.commit()


lukuvinkki_repository = LukuvinkkiRepository()
