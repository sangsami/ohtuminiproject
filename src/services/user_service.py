from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    def __init__(self, user_repository, user_model):
        self._user_repository = user_repository
        self._user_model = user_model

    def check_credentials(self, username, password):
        user = self._user_repository.find_by_username(username)

        if not user or not check_password_hash(user.password, password):
            return None

        return user

    def get_user(self, user_id):
        return self._user_repository.find_by_id(user_id)

    def create_user(self, username, password):
        user = self._user_repository.create(
            self._user_model(
                username,
                generate_password_hash(password, method='sha256'))
        )

        return user

    def check_if_unique_username(self, username):
        if self._user_repository.find_by_username(username):
            return False
        return True
