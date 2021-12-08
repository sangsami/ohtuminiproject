from werkzeug.security import generate_password_hash
from app import app, db
from models.user import User

db.create_all(app=app)
db.session.commit()

guest = User('guest', generate_password_hash('veryStrongPassword', method='sha256'))
db.session.add(guest)
db.session.commit()
