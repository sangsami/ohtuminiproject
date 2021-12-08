class UserRepository:
    def __init__(self, db_, user_model):
        self._db = db_
        self._user_model = user_model

    def find_users(self):
        return self._db.session.query(self._user_model).all()

    def find_by_username(self, username):
        return self._db.session.query(self._user_model).filter_by(username=username).first()

    def create(self, user):
        existing_user = self.find_by_username(user.username)

        if existing_user:
            return None

        self._db.session.add(user)
        self._db.session.commit()

        return user

    def delete(self, user_id):
        pass
