from datetime import datetime
import pytz
from pytz import timezone
from app import db
# pylint: disable=no-member, disable=too-many-arguments
class Lukuvinkki(db.Model):
    __tablename__ = "lukuvinkki"
    lukuvinkki_id = db.Column(db.Integer, primary_key=True)
    lukuvinkki_type = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=True)
    isbn = db.Column(db.String(80), nullable=True)
    is_read = db.Column(db.Boolean, nullable=False, default=False)
    is_public = db.Column(db.Boolean, nullable=False, default=False)
    link = db.Column(db.String(120), nullable=True)
    descript = db.Column(db.String(500), nullable=True)
    comment = db.Column(db.String(500), nullable=True)
    read_timestamp = db.Column(db.DateTime(timezone = True), nullable =True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(
            self,
            title,
            author,
            isbn,
            link,
            description,
            comment,
            user_id,
            is_public=None,
            lukuvinkki_type=None,
            is_read=None
            ):
        if is_public is None:
            is_public = False
        if lukuvinkki_type is None:
            lukuvinkki_type = "Book"
        if is_read is None:
            is_read = False
        self.title = title
        self.author = author
        self.isbn = isbn
        self.descript = description
        self.link = link
        self.comment = comment
        self.user_id = user_id
        self.is_public = is_public
        self.lukuvinkki_type = lukuvinkki_type
        self.is_read = is_read
        self.read_timestamp = None

    def read_status(self):
        if self.read_timestamp is not None:
            reading_time = self.read_timestamp.astimezone(timezone('Europe/Helsinki'))
            reading_time = reading_time.strftime("%d.%m.%y  %H:%M")
        return f"Read - {reading_time:>15}" if self.is_read else "Not read"

    def change_read(self):
        self.is_read = not self.is_read
        self.read_timestamp = datetime.now(pytz.timezone('Europe/Helsinki'))
        print(self.read_timestamp)

    def __str__(self):
        return f"{self.lukuvinkki_type}: {self.title}"
