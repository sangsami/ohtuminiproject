from flask import (
    Flask,
    render_template,
)

app = Flask(__name__)

@app.route("/")
def render_home():
    return render_template("index.html")

@app.route("/ping")
def ping():
    return "Pong"