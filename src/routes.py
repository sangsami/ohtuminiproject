from flask import  (
    Flask,
    render_template,
    request,
    redirect,
    flash
)
from app import app
from services.lukuvinkki_service import lukuvinkki_service

@app.route("/")
def render_home():
    return render_template("index.html")

@app.route("/lukuvinkki", methods=["GET"])
def render_lukuvinkki():
    return render_template("lukuvinkki.html")

@app.route("/lukuvinkki", methods=["POST"])
def handle_lukuvinkki():
    title = request.form.get("title")
    author = request.form.get("author")
    description = request.form.get("description")
    link = request.form.get("link")
    comment = request.form.get("comment")
    
    try:
        lukuvinkki_service.create_lukuvinkki(title, author, description, link, comment)
        flash("The lukuvinkki was saved.")
    except Exception as error:
        flash(str(error))

    return redirect("/lukuvinkki")

@app.route("/ping")
def ping():
    return "Pong"