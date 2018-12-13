from flask import Blueprint, render_template, request, current_app, url_for, redirect
from app.models import Direction
from app.form.direction_manage_form import CreateForm
from app import db


main = Blueprint('direction', __name__)


@main.route('/', methods=['GET'])
def directions():
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['PER_PAGE']
    pagination = Direction.query.order_by(Direction.id.asc()).paginate(page, per_page=per_page)
    direction_all = pagination.items
    return render_template('backmanage/direction/all.html', directions=direction_all, pagination=pagination)


@main.route('/add', methods=['GET', 'POST'])
def add():
    create_form = CreateForm()
    if request.method == 'POST' and create_form.validate():
        print("验证成功")
        id = create_form.id.data
        name = create_form.name.data
        content = create_form.content.data
        direction = Direction(id=id, name=name, content=content)
        db.session.add(direction)
        db.session.commit()
        return redirect(url_for('direction.directions'))
    return render_template('backmanage/direction/add.html', form=create_form)
