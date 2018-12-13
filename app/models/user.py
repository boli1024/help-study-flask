from app import db
from app import login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    number = db.Column(db.String(8), unique=True)
    password = db.Column(db.String(64))
    directionId = db.Column(db.Integer, db.ForeignKey('direction.id'))

    def __repr__(self):
        return '<user %r>' % self.username


# 加载用户的回调函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))