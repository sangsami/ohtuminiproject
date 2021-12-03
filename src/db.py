from app import app
from flask_sqlalchemy import SQLAlchemy
import fixforheroku

app.config["SQLALCHEMY_DATABASE_URI"] = fixforheroku.uri 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)