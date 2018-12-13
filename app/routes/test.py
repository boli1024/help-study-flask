from flask import Blueprint, render_template

test = Blueprint("test", __name__)


@test.route('/t1', methods=['GET'])
def test1():
    return render_template("test/test1.html")
