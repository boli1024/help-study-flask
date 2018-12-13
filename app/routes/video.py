from flask import (
    render_template,
    Blueprint,
    request
)
from ..data.video import video_data


main = Blueprint('video', __name__)


@main.route('/', methods=['GET'])
def play():
    return render_template("play.html")


@main.route('/src', methods=['POST'])
def src():
    form = request.form
    name = form.get('name')
    return video_data[name]
