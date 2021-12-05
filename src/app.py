from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import fixforheroku

app = Flask(__name__)
app.secret_key = "this_will_need_to_be_changed_in_production"

app.config["SQLALCHEMY_DATABASE_URI"] = fixforheroku.uri 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

# pylint: disable=wrong-import-position
# pylint: disable=unused-import
import routes
# pylint: enable=unused-import
# pylint: enable=wrong-import-position

# Blueprint for auth routes
from auth.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
