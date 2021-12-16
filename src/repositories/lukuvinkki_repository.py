from entities.lukuvinkki import Lukuvinkki  # pylint: disable=unused-import
from app import db

# pylint: disable=line-too-long
class LukuvinkkiRepository:
    def __init__(self):
        pass

    def get_books(self, user_id, searchterm=""):
        return Lukuvinkki.query.filter((Lukuvinkki.lukuvinkki_type == "Book") & (Lukuvinkki.user_id == user_id)).filter(Lukuvinkki.title.ilike("%" + searchterm +"%")).order_by(Lukuvinkki.lukuvinkki_id.desc()).all()

    def get_blog_posts(self, user_id, searchterm=""):
        return Lukuvinkki.query.filter((Lukuvinkki.lukuvinkki_type == "Blog post") & (Lukuvinkki.user_id == user_id)).filter(Lukuvinkki.title.ilike("%" + searchterm +"%")).order_by(Lukuvinkki.lukuvinkki_id.desc()).all()

    def get_podcasts(self, user_id, searchterm=""):
        return Lukuvinkki.query.filter((Lukuvinkki.lukuvinkki_type == "Podcast") & (Lukuvinkki.user_id == user_id)).filter(Lukuvinkki.title.ilike("%" + searchterm +"%")).order_by(Lukuvinkki.lukuvinkki_id.desc()).all()

    def get_youtubes(self, user_id, searchterm=""):
        return Lukuvinkki.query.filter((Lukuvinkki.lukuvinkki_type == "Youtube") & (Lukuvinkki.user_id == user_id)).filter(Lukuvinkki.title.ilike("%" + searchterm +"%")).order_by(Lukuvinkki.lukuvinkki_id.desc()).all()

    def get_publics(self, user_id, searchterm=""):
        return Lukuvinkki.query.filter((Lukuvinkki.user_id != user_id) & (Lukuvinkki.is_public == True)).filter(Lukuvinkki.title.ilike("%" + searchterm +"%")).order_by(Lukuvinkki.lukuvinkki_id.desc()).all()
        
    def find_all(self):
        return Lukuvinkki.query.order_by(Lukuvinkki.lukuvinkki_id.desc()).all()

# pylint: disable=too-many-arguments

    def create(self, lukuvinkki):
        db.session.add(lukuvinkki)
        db.session.commit()

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
        lukuvinkki = self.get_lukuvinkki(lukuvinkki_id)
        lukuvinkki.title = title
        lukuvinkki.author = author
        lukuvinkki.isbn = isbn
        lukuvinkki.link = link
        lukuvinkki.descript = description
        lukuvinkki.comment = comment
        lukuvinkki.is_public = is_public
        lukuvinkki.lukuvinkki_type = lukuvinkki_type
        db.session.commit()

# pylint: disable=line-too-long

    def check_lukuvinkki(self, title, user_id, lukuvinkki_type):
        query_title = Lukuvinkki.query.filter(Lukuvinkki.title == title).first()
        if query_title is not None and query_title.user_id == user_id and query_title.lukuvinkki_type == lukuvinkki_type:
            return True
        return False

    def get_lukuvinkki(self, lukuvinkki_id):
        return Lukuvinkki.query.get(lukuvinkki_id)

    def change_lukuvinkki_status(self, lukuvinkki_id):
        lukuvinkki = self.get_lukuvinkki(lukuvinkki_id)
        lukuvinkki.change_read()
        db.session.commit()

    def delete_lukuvinkki(self, lukuvinkki_id):
        record_obj = Lukuvinkki.query.filter(Lukuvinkki.lukuvinkki_id==lukuvinkki_id).first()
        db.session.delete(record_obj)
        db.session.commit()


lukuvinkki_repository = LukuvinkkiRepository()
