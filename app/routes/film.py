from flask import (
    render_template,
    redirect,
    request,
    Blueprint,
    url_for,
)


main = Blueprint('film', __name__)


@main.route('search', methods=['GET'])
def search():
    return render_template("film.html")


@main.route('result', methods=['POST'])
def result():
    form = request.form
    film_name = form.get('filmname')
    return render_template("root.html", content=film_name)
