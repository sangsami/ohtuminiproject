from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    time_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())

    def __repr__(self) -> str:
        return f"<User(username={self.username}, time_created={self.time_created})>"