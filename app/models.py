from . import db
from . import login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    number = db.Column(db.String(8), unique=True)
    password = db.Column(db.String(64))
    directionId = db.Column(db.Integer, db.ForeignKey('direction.id'))


class Progress(db.Model):
    __tablename__ = 'progress'
    id = db.Column(db.Integer, primary_key=True)


class Direction(db.Model):
    __tablename__ = 'direction'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    content = db.Column(db.Text)

    users = db.relationship('User', backref='direction', lazy='dynamic')
    courses = db.relationship('Course', backref='direction', lazy='dynamic')


class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    cycle = db.Column(db.Integer)

    directionId = db.Column(db.Integer, db.ForeignKey('direction.id'))


# 加载用户的回调函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
