from flask import (
    Blueprint,
    render_template,
    url_for,
    redirect,
    request,
    flash
)
from auth.forms import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User

from repositories.user_repository import user_repository
from services.user_service import user_service

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register_post():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        new_user = user_service.create_user(form.username.data, form.password.data)
        if new_user:
            flash('Thanks for registering')
            return redirect(url_for('auth.login'))
        else:
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

    return redirect(url_for('render_lukuvinkkiview'))

@auth.route('/logout')
def logout():
    return 'Logout'

