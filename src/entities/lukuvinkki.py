from app import db
import enum

class Lukuvinkki(db.Model):
    __tablename__ = "lukuvinkki"
    id = db.Column(db.Integer, primary_key = True)
    current_type = db.Column(db.String(10), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(100), nullable = True)
    is_read = db.Column(db.Boolean, nullable = False)
    link = db.Column(db.String(120), nullable = True)
    descript = db.Column(db.String(500), nullable = True)
    comment = db.Column(db.String(500), nullable = True)

    def __init__(
            self,
            title,
            author,
            link,
            description,
            comment,
            type=None,
            is_read=None
            ):
        if is_read is None:
            self.read = False
        if type is None:
            self.current_type = "Book"
        self.current_type = type
        self.title = title
        self.author = author
        self.descript = description
        self.link = link
        self.comment = comment
        self.current_type = type

    def read_status(self):
        return "Read" if self.is_read else "Not read"

    def change_read(self):
        self.is_read = not self.is_read

    def __str__(self):
        return f"{self._title} {self._author}"
