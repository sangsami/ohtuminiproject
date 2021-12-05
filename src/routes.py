from flask import (
    render_template,
    request,
    redirect,
    flash
)
from app import app
from repositories.lukuvinkki_repository import lukuvinkki_repository
from services.lukuvinkki_service import (
    lukuvinkki_service,
    LukuvinkkiExistsError,
    LukuvinkkiTitleOrAuthor
)

from db import db

#This route is just for demonstrating the usage of the db in this code:
@app.route("/example_db_ops")
def example_db_ops():
    lukuvinkki_service.example_db_ops()
    return "tested db -- check db"

@app.route("/")
def render_home():
    return render_template("index.html")


@app.route("/addlukuvinkki", methods=["GET"])
def render_addlukuvinkki():
    return render_template("addlukuvinkki.html")


@app.route("/addlukuvinkki", methods=["POST"])
def handle_addlukuvinkki():
    if "view_button" in request.form:
        return redirect("/lukuvinkkiview")

    if "save_button" in request.form:
        title = request.form.get("title")
        author = request.form.get("author")
        description = request.form.get("description")
        link = request.form.get("link")
        comment = request.form.get("comment")

        try:
            lukuvinkki_service.create_lukuvinkki(
                title, author, description, link, comment)
            flash("The lukuvinkki was saved.")
        except (LukuvinkkiTitleOrAuthor, LukuvinkkiExistsError) as error:
            flash(str(error))

    return redirect("/addlukuvinkki")


@app.route("/lukuvinkkiview")
def render_lukuvinkkiview():
    all_lukuvinkki = lukuvinkki_service.get_lukuvinkkis()
    return render_template(
        "lukuvinkkiview.html", all_lukuvinkki=all_lukuvinkki)


@app.route("/ping")
def ping():
    return "Pong"


@app.route("/tests/reset", methods=["POST"])
def reset_tests():
    lukuvinkki_repository.delete_all()
    return "Reset"
