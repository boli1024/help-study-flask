from flask import Blueprint, render_template, redirect, url_for
from app.models import Direction, Plan
from app import db
from flask_login import current_user, login_required
import json


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


@login_required
@main.route('getDirectionDetails', methods=['GET'])
def get_direction_details():
    data = []
    details = current_user.direction.details
    for detail in details:
        data.append(detail.name)
    #  return data.__str__()   视图函数的返回值必须为字符串，故使用列表的 __str__() 方法将其转换为字符串
    #  将字符串传到前端时，格式为['1','2']，其中的单引号需要转为双引号才能将 data 序列化为数组，过程繁琐，故使用 json 序列化列表，格式为 ["1","2"]
    return json.dumps(data)


# 获取理想计划的时间节点
@login_required
@main.route('getIdealPlanDate', methods=['GET'])
def get_ideal_plan_date():
    date = []
    plans = current_user.plans
    index = 1
    for plan in plans:
        if index == 1:
            date.append(str(plan.beginTime))
            date.append(str(plan.endTime))
            index += 1
        else:
            date.append(str(plan.endTime))
    return json.dumps(date)


# 获取实际的学习时间节点
@login_required
@main.route('getActualPlanDate', methods=['GET'])
def get_actual_plan_date():
    date = []
    index = 1
    plans = current_user.plans
    for plan in plans:
        if index == 1:
            date.append(str(plan.beginTime))
            index += 2
        if plan.state == 1:
            date.append(str(plan.actualEndTime))
    return json.dumps(date)


@login_required
@main.route('finishPlan/<int:id>', methods=['GET'])
def finish_plan(id):
    plans = current_user.plans
    for plan in plans:
        if plan.id == id:
            plan.__setstate__(1)
        if plan.id == id+1:
            plan.__setstate__(2)
    return redirect(url_for('project.make_plan'))


@login_required
@main.route('appointPlanEnd/<int:plan_id>/<int:year>/<int:month>/<int:day>', methods=['GET'])
def appoint_plan_end(plan_id, year, month, day):
    plan = Plan.query.get_or_404(plan_id)
    plan.set_actual_end_time(year=year, month=month, day=day)
    return redirect(url_for('project.make_plan'))
