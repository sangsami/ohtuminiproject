from flask import Flask
import routes

app = Flask(__name__)
app.secret_key = "this_will_need_to_be_changed_in_production"
