from app import db
from .plan import Plan
from flask_login import current_user
from datetime import date, timedelta


class Direction(db.Model):
    __tablename__ = 'direction'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    content = db.Column(db.Text, nullable=False)

    users = db.relationship('User', back_populates='direction', lazy='dynamic')
    details = db.relationship('DirectionDetail', back_populates='direction')

    def __repr__(self):
        return '<direction %r>' % self.name

    def create_plans(self):
        current_user.delete_plans()
        begin = date.today()
        for detail in self.details:
            days = int(current_user.studyDays * (detail.weight/100))
            end = begin + timedelta(days)
            plan = Plan(user=current_user, directionDetail=detail, days=days,
                        beginTime=begin, endTime=end+timedelta(-1))
            db.session.add(plan)
            begin = end
        db.session.commit()
