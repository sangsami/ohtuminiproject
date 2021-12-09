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
    LukuvinkkiTitle
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
    return render_addlukuvinkki(type=type)

@app.route("/changetype", methods=["POST"])
@login_required
def handle_changetype():
    type = request.form["type"]
    lukuvinkki_id = request.form["lukuvinkki"]
    lukuvinkki = lukuvinkki_repository.get_lukuvinkki(lukuvinkki_id)
    return render_template("/changelukuvinkki.html", type=type, lukuvinkki=lukuvinkki)

@app.route("/addlukuvinkki")
@login_required
def render_addlukuvinkki(type=None):
    if type is None:
        type = "Book"
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
        except (LukuvinkkiTitle, LukuvinkkiExistsError) as error:
            flash(str(error))
        return render_template("addlukuvinkki.html", type=type)

@app.route("/changelukuvinkki", methods=["POST"])
@login_required
def handle_changelukuvinkki():
    if "view_button" in request.form:
        return render_lukuvinkkiview()
    else:
        id = request.form.get("id")
        type = request.form["type"]
        title = request.form.get("title")
        author = request.form.get("author")
        description = request.form.get("description")
        link = request.form.get("link")
        comment = request.form.get("comment")

        try:
            lukuvinkki_service.change_lukuvinkki(
                id, title, author, link, description, comment, type)
            flash("The lukuvinkki was saved.")
        except (LukuvinkkiTitle, LukuvinkkiExistsError) as error:
            flash(str(error))
        return render_template("index.html")

@app.route("/lukuvinkkiview", methods=["GET"])
@login_required
def render_lukuvinkkiview():
    books = lukuvinkki_service.get_books()
    blog_posts = lukuvinkki_service.get_blog_posts()
    podcasts = lukuvinkki_service.get_podcasts()
    youtubes = lukuvinkki_service.get_youtubes()
    return render_template(
        "lukuvinkkiview.html", books=books, blog_posts=blog_posts,
        podcasts=podcasts, youtubes=youtubes)

@app.route("/lukuvinkkiview", methods=["POST"])
@login_required
def handle_lukuvinkkiview():
    if "change_status_button" in request.form:
        id = request.form.get("lukuvinkki_id")
        lukuvinkki_service.change_lukuvinkki_status(id)
        return redirect("/lukuvinkkiview")
    elif "edit_button" in request.form:
        id = request.form.get("lukuvinkki_id")
        lukuvinkki = lukuvinkki_repository.get_lukuvinkki(id)
        return render_template("/changetype.html", lukuvinkki=lukuvinkki)


@app.route("/ping")
def ping():
    return "Pong"


@app.route("/tests/reset", methods = ["POST"])
def reset_tests():
    lukuvinkki_repository.delete_all()
    return "Reset"
