from werkzeug.security import generate_password_hash
from app import app, db

db.drop_all(app=app)
db.session.commit()
