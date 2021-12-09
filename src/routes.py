from flask import (
    render_template,
    request,
    redirect,
    flash
)
from flask_login import login_required
from app import app
from repositories.lukuvinkki_repository import lukuvinkki_repository
from services.lukuvinkki_service import (
    lukuvinkki_service,
    LukuvinkkiExistsError,
    LukuvinkkiTitleOrAuthor
)

#This route is just for demonstrating the usage of the db in this code:
@app.route("/example_db_ops")
def example_db_ops():
    lukuvinkki_service.example_db_ops()
    return "tested db -- check db"

@app.route("/")
def render_home():
    return render_template("index.html")

@app.route("/choosetype")
@login_required
def render_choosetype():
    return render_template("choosetype.html")

@app.route("/choosetype", methods=["POST"])
@login_required
def handle_choosetype():
    type = request.form["type"]
    return render_addlukuvinkki(type)

@app.route("/addlukuvinkki")
@login_required
def render_addlukuvinkki(type):
    return render_template("addlukuvinkki.html", type=type)

@app.route("/addlukuvinkki", methods=["POST"])
@login_required
def handle_addlukuvinkki():
    if "view_button" in request.form:
        return render_lukuvinkkiview()
    else:
        type = request.form["type"]
        title = request.form.get("title")
        author = request.form.get("author")
        description = request.form.get("description")
        link = request.form.get("link")
        comment = request.form.get("comment")

        try:
            lukuvinkki_service.create_lukuvinkki(
                title, author, link, description, comment, type)
            flash("The lukuvinkki was saved.")
        except (LukuvinkkiTitleOrAuthor, LukuvinkkiExistsError) as error:
            flash(str(error))
        return redirect("/addlukuvinkki")

@app.route("/lukuvinkkiview", methods=["GET"])
@login_required
def render_lukuvinkkiview():
    all_lukuvinkki = lukuvinkki_service.get_lukuvinkkis()
    return render_template(
        "lukuvinkkiview.html", all_lukuvinkki=all_lukuvinkki)

@app.route("/lukuvinkkiview", methods=["POST"])
@login_required
def handle_lukuvinkkiview():
    if "change_status_button" in request.form:
        id = request.form.get("lukuvinkki_id")
        lukuvinkki_service.change_lukuvinkki_status(id)
        return redirect("/lukuvinkkiview")


@app.route("/ping")
def ping():
    return "Pong"


@app.route("/tests/reset", methods = ["POST"])
def reset_tests():
    lukuvinkki_repository.delete_all()
    return "Reset"
