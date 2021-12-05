from flask import (
    Blueprint, 
    render_template, 
    url_for, 
    redirect, 
    request,
    flash
)
from models.user import User
# import database, db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    
    # tässä tarkistetaan myös salasanan hash, kunhan register on tehty
    # if not user or not check_password_hash(user.password, password)
    if not user:
        flash('Invalid username or password')
        return redirect(url_for('auth.login'))

    return redirect(url_for('render_home'))

@auth.route('/logout')
def logout():
    return 'Logout'
