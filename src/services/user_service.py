from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
    )

class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        user = self._user_repository.find_by_username(username)

        if not user or not check_password_hash(user.password, password):
            return None

        return user

    def create_user(self, username, password):
        user = self._user_repository.create(
            User(username=username, password=generate_password_hash(password, method='sha256'))
        )

        return user

    def check_if_unique_username(self, username):
        if self._user_repository.find_by_username(username):
            return False
        return True

user_service = UserService()
