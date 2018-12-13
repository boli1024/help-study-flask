from ..data.direction import directions
from ..ext import read_course, read_html
from flask import (
    render_template,
    redirect,
    Blueprint,
    request,
    url_for,
)


main = Blueprint('project', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@main.route('/about2', methods=['GET'])
def about2():
    return render_template('about2.html')


@main.route('/about3', methods=['GET'])
def about3():
    return render_template('about3.html')


@main.route('/plan', methods=['GET'])
def make_plan():
    return render_template('make_plan.html')


@main.route('/direction', methods=['GET'])
def direction():
    return render_template('direction.html')


@main.route('/detail', methods=['POST'])
def detail():
    form = request.form
    name = form.get('name')
    data = directions[name]
    return data


@main.route('/progress', methods=['GET'])
def progress():
    return render_template('progress.html')


@main.route('/study', methods=['GET'])
def study():
    courses = read_course()
    return render_template('study/html.html', courses=courses)

