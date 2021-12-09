from werkzeug.security import generate_password_hash
from app import app, db
from models.user import User

db.create_all(app=app)
db.session.commit()

#test if the db is already initialized and guestuser created
guest = db.session.query(User).filter_by(username='guest').first()

if not guest:
    guest = User('guest', generate_password_hash('veryStrongPassword', method='sha256'))
    db.session.add(guest)
    db.session.commit()
