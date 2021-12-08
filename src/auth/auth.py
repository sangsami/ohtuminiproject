from flask import (
    Blueprint,
    render_template,
    url_for,
    redirect,
    request,
    flash
)
from flask_login import login_user, logout_user
from auth.forms import RegistrationForm
from models.user import User

from app import db
from repositories.user_repository import UserRepository
from services.user_service import UserService

user_repository = UserRepository(db, User)
user_service = UserService(user_repository, User)


auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register_post():
    form = RegistrationForm(request.form, user_service)
    if request.method == 'POST' and form.validate():
        new_user = user_service.create_user(form.username.data, form.password.data)
        if new_user:
            flash('Thanks for registering')
            return redirect(url_for('auth.login'))

        flash('Username already in use')
        return render_template('register.html', form=form)

    return render_template('register.html', form=form)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():

    username = request.form.get('username')
    password = request.form.get('password') # pylint: disable=unused-variable
    # form-validation

    user = user_service.check_credentials(username, password)

    if not user:
        flash('Invalid username or password')
        return redirect(url_for('auth.login'))

    login_user(user)
    return redirect(url_for('render_lukuvinkkiview'))

@auth.route('/logout')
def logout():
    logout_user()
    return 'Logout'
