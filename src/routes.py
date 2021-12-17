from flask import (
    render_template,
    request,
    redirect,
    flash
)
import requests
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
        return redirect("/lukuvinkkiview")
    return redirect("/login")

@app.route("/choosetype")
@login_required
def render_choosetype():
    return render_template("choosetype.html")

@app.route("/choosetype", methods=["POST"])
@login_required
def handle_choosetype():
    lukuvinkki_type = request.form["type"]
    url = request.form['youtube-url']
    if lukuvinkki_type == 'Youtube' and url:
        data = get_youtube_information_from_url(url)
        if data:
            return render_addlukuvinkki(lukuvinkki_type=lukuvinkki_type, youtube_data=data)
        flash('Could not find any youtube videos with provided url')
    return render_addlukuvinkki(lukuvinkki_type=lukuvinkki_type)

def get_youtube_information_from_url(video_url):
    url = f'https://www.youtube.com/oembed?url={video_url}&format=json'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    json_data = response.json()
    json_data['url'] = video_url

    return json_data

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
def render_addlukuvinkki(lukuvinkki_type=None, youtube_data=None):
    if lukuvinkki_type is None:
        lukuvinkki_type = "Book"
    return render_template(
        "addlukuvinkki.html",
        lukuvinkki_type=lukuvinkki_type,
        youtube_data=youtube_data
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
    is_public = request.form.get("visibility") is not None

    try:
        lukuvinkki_service.create_lukuvinkki(
            title,
            author,
            isbn,
            link,
            description,
            comment,
            current_user.id,
            is_public,
            lukuvinkki_type
            )
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
    is_public = request.form.get("visibility") is not None

    try:
        lukuvinkki_service.change_lukuvinkki(
            lukuvinkki_id,
            title,
            author,
            isbn,
            link,
            description,
            comment,
            is_public,
            lukuvinkki_type
            )
        flash("The lukuvinkki was saved.")
    except (LukuvinkkiTitle, LukuvinkkiExistsError) as error:
        flash(str(error))
    return redirect("/lukuvinkkiview")

@app.route("/lukuvinkkiview", methods=["GET"])
@login_required
def render_lukuvinkkiview():
    user_id = current_user.id
    books = lukuvinkki_service.get_books(user_id)
    blog_posts = lukuvinkki_service.get_blog_posts(user_id)
    podcasts = lukuvinkki_service.get_podcasts(user_id)
    youtubes = lukuvinkki_service.get_youtubes(user_id)
    publics = lukuvinkki_service.get_publics(user_id)
    return render_template(
        "lukuvinkkiview.html",
        user_id=user_id,
        books=books,
        blog_posts=blog_posts,
        podcasts=podcasts,
        youtubes=youtubes,
        publics=publics
        )

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

@app.route("/search", methods=["GET"])
@login_required
def render_searchview():
    return render_template(
        "search.html")

@app.route("/search", methods=["POST"])
@login_required
def handle_search():
    searchterm = request.form.get("searchterm")
    return redirect(
        "/lukuvinkkiresult?searchterm=" + searchterm)

@app.route("/lukuvinkkiresult")
def render_lukuvinkkisearchview():
    searchterm = request.args.get('searchterm')
    if not searchterm:
        searchterm = ""
    user_id = current_user.id
    books = lukuvinkki_service.get_books(user_id, searchterm)
    blog_posts = lukuvinkki_service.get_blog_posts(user_id, searchterm)
    podcasts = lukuvinkki_service.get_podcasts(user_id, searchterm)
    youtubes = lukuvinkki_service.get_youtubes(user_id, searchterm)
    publics = lukuvinkki_service.get_publics(user_id, searchterm)
    result = (len(books)+len(blog_posts)+len(podcasts)+len(youtubes)+len(publics)) > 0 # pylint: disable=line-too-long
    return render_template(
        "searchresult.html", result=result, books=books, blog_posts=blog_posts,
        podcasts=podcasts, youtubes=youtubes, publics=publics)

@app.route("/ping")
def ping():
    return "Pong"
