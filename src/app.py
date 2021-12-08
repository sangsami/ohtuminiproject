from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import fixforheroku
from config import SECRET
from repositories.user_repository import UserRepository
from services.user_service import UserService
from models.user import User

app = Flask(__name__)
app.secret_key = SECRET

app.config["SQLALCHEMY_DATABASE_URI"] = fixforheroku.uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

user_repository = UserRepository(db, User)
user_service = UserService(user_repository, User)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return user_service.get_user(user_id)

# pylint: disable=wrong-import-position
# pylint: disable=unused-import
import routes
# pylint: enable=unused-import


# Blueprint for auth routes
from auth.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# pylint: enable=wrong-import-position
