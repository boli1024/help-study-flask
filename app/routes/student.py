from flask import Blueprint, render_template, redirect, url_for
from app.models import Direction
from app import db
from flask_login import current_user, login_required


main = Blueprint('student', __name__)


@login_required
@main.route('/profile', methods=['GET'])
def profile():
    return render_template('student/profile.html', current_user=current_user)


@login_required
@main.route('setDirection/<int:id>', methods=['GET', 'POST'])
def set_direction(id):
    direction = Direction.query.get_or_404(id)
    if direction is None:
        raise 500
    current_user.direction = direction
    current_user.set_study_days()
    db.session.add(current_user)
    current_user.direction.create_plans()
    return redirect(url_for('project.make_plan'))
