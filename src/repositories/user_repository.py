from models.user import User
from app import db as default_db

class UserRepository:
    def __init__(self, db=default_db):
        self._db = db

    def find_users(self):
        return self._db.session.query(User).all()

    def find_by_username(self, username):
        return self._db.session.query(User).filter_by(username=username).first()

    def create(self, user):
        existing_user = self.find_by_username(user.username)

        if existing_user:
            return None

        self._db.session.add(user)
        self._db.session.commit()

        return user

    def delete(self, user_id):
        pass

user_repository = UserRepository()
