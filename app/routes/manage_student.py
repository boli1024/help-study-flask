from flask import Blueprint, render_template
from app.models import User


main = Blueprint("student", __name__)


@main.route("/", methods=['GET'])
def students():
    users = User.query.order_by(User.id.asc())
    return render_template("backmanage/student/all.html", users=users)
