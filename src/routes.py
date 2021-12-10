from flask import (
    render_template,
    request,
    redirect,
    flash
)
from flask_login import login_required, current_user
from app import app
from repositories.lukuvinkki_repository import lukuvinkki_repository
from services.lukuvinkki_service import (
    lukuvinkki_service,
    LukuvinkkiExistsError,
    LukuvinkkiTitle
)

@app.route("/")
def render_home():
    if current_user.is_authenticated:
        return render_template("index.html", name=current_user.username)
    return redirect("/login")

@app.route("/choosetype")
@login_required
def render_choosetype():
    return render_template("choosetype.html")

@app.route("/choosetype", methods=["POST"])
@login_required
def handle_choosetype():
    lukuvinkki_type = request.form["type"]
    return render_addlukuvinkki(lukuvinkki_type=lukuvinkki_type)

@app.route("/changetype", methods=["POST"])
@login_required
def handle_changetype():
    lukuvinkki_type = request.form["type"]
    lukuvinkki_id = request.form["lukuvinkki_id"]
    lukuvinkki = lukuvinkki_repository.get_lukuvinkki(lukuvinkki_id)
    return render_template(
        "/changelukuvinkki.html",
        lukuvinkki_type=lukuvinkki_type,
        lukuvinkki=lukuvinkki
        )

@app.route("/addlukuvinkki")
@login_required
def render_addlukuvinkki(lukuvinkki_type=None):
    if lukuvinkki_type is None:
        lukuvinkki_type = "Book"
    return render_template(
        "addlukuvinkki.html",
        lukuvinkki_type=lukuvinkki_type
        )

@app.route("/addlukuvinkki", methods=["POST"])
@login_required
def handle_addlukuvinkki():
    if "view_button" in request.form:
        return render_lukuvinkkiview()
    lukuvinkki_type = request.form["type"]
    title = request.form.get("title")
    author = request.form.get("author")
    isbn = request.form.get("ISBN")
    description = request.form.get("description")
    link = request.form.get("link")
    comment = request.form.get("comment")

    try:
        lukuvinkki_service.create_lukuvinkki(
            title, author, isbn, link, description, comment, lukuvinkki_type)
        flash("The lukuvinkki was saved.")
    except (LukuvinkkiTitle, LukuvinkkiExistsError) as error:
        flash(str(error))
    return render_template(
        "addlukuvinkki.html",
        lukuvinkki_type=lukuvinkki_type
        )

@app.route("/changelukuvinkki", methods=["POST"])
@login_required
def handle_changelukuvinkki():
    if "view_button" in request.form:
        return render_lukuvinkkiview()
    lukuvinkki_id = request.form.get("lukuvinkki_id")
    lukuvinkki_type = request.form["type"]
    title = request.form.get("title")
    author = request.form.get("author")
    isbn = request.form.get("ISBN")
    description = request.form.get("description")
    link = request.form.get("link")
    comment = request.form.get("comment")

    try:
        lukuvinkki_service.change_lukuvinkki(
            lukuvinkki_id,
            title,
            author,
            isbn,
            link,
            description,
            comment,
            lukuvinkki_type
            )
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
        lukuvinkki_id = request.form.get("lukuvinkki_id")
        lukuvinkki_service.change_lukuvinkki_status(lukuvinkki_id)
        return redirect("/lukuvinkkiview")
    if "edit_button" in request.form:
        lukuvinkki_id = request.form.get("lukuvinkki_id")
        lukuvinkki = lukuvinkki_repository.get_lukuvinkki(lukuvinkki_id)
        return render_template("/changetype.html", lukuvinkki=lukuvinkki)
    return redirect("/lukuvinkkiview")

@app.route("/lukuvinkkisearch")
def render_lukuvinkkisearchview():
    searchterm = request.args.get('searchterm')
    if not searchterm:
        searchterm = ""
    result = lukuvinkki_service.find_by_name(searchterm)
    return render_template(
        "lukuvinkkiview.html", books=result, blog_posts=None,
        podcasts=None, youtubes=None)

@app.route("/ping")
def ping():
    return "Pong"


@app.route("/tests/reset", methods=["POST"])
def reset_tests():
    lukuvinkki_repository.delete_all()
    return "Reset"
