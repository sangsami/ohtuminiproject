from flask import (
    Blueprint,
    render_template,
    url_for,
    redirect,
    request,
    flash
)
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/register')
def register():
    return render_template('register.html')

@auth.route('/register', methods=['POST'])
def register_post():

    username = request.form.get('username')
    password = request.form.get('password')
    password_confirmation = request.form.get('password_confirmation')

    user = find_user_by_username(username)

    errors = False
    if user:
        flash('Username already in use')
        errors = True

    if password != password_confirmation:
        flash("Passwords don't match")
        errors = True

    if errors:
        return redirect(url_for('auth.register'))

    new_user = User(username=username, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():

    username = request.form.get('username')
    password = request.form.get('password') # pylint: disable=unused-variable

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Invalid username or password')
        return redirect(url_for('auth.login'))

    return redirect(url_for('render_lukuvinkkiview'))

@auth.route('/logout')
def logout():
    return 'Logout'

def find_user_by_username(username):
    return User.query.filter_by(username=username).first()
