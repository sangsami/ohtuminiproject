from wtforms import Form, StringField, PasswordField, validators, ValidationError

class RegistrationForm(Form):
    def __init__(self, form, user_service):
        super().__init__(form)
        self._user_service = user_service

    username = StringField('Username', [
        validators.Length(min=4, message='Username needs to be 4 characters long or longer'),
        validators.DataRequired(message='Username is required'),
        validators.Regexp('^[a-zA-Z]+$', message='Username must contain only letters from a to z')
    ])

    def validate_username(self, field):
        if not self._user_service.check_if_unique_username(field.data):
            self.username.errors += (ValidationError('Username already in use'),)

    password = PasswordField('Password', [
        validators.Length(min=8, message='Password needs to be 8 characters long or longer'),
        validators.DataRequired(message='Password is required'),
        validators.Regexp('^.*\d.*[A-Z].*|.*[A-Z].*\d.*$', message='Password must be alpha numeric'),
        validators.EqualTo('password_confirmation', message='Passwords must match')
    ])

    password_confirmation = PasswordField('Repeat Password', [
        validators.DataRequired(message='Repeat password')
    ])
