from flask import Blueprint
# import database, db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/logout')
def logout():
    return 'Logout'
