from app import db
from app import login_manager
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    number = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(64), nullable=False)
    directionId = db.Column(db.Integer, db.ForeignKey('direction.id'))

    direction = db.relationship('Direction', back_populates='users')
    plans = db.relationship('Plan', back_populates='user', lazy='dynamic')

    beginStudyTime = db.Column(db.String(10))
    endStudyTime = db.Column(db.String(10))
    studyDays = db.Column(db.Integer)  # 学习天数,当学生选择岗位方向时自动设置

    studyTimeTag = db.Column(db.Integer, default=0)  # 学习时间是否设置的标记，1 已设置   0 未设置

    role = db.Column(db.Integer, nullable=False)  # 1.学生 2.教师 3.管理员

    def __repr__(self):
        if self.role == 1:
            return '<student %r>' % self.username
        if self.role == 2:
            return '<teacher %r>' % self.username
        return '<user %r>' % self.username

    def set_study_time(self):  # 根据学号设置入学时间以及毕业时间
        if self.role == 1:
            year = self.number[0:4]
            self.beginStudyTime = year + '-9-1'
            self.endStudyTime = str(int(year) + 4) + '-6-1'

    def set_study_days(self):  # 设置当前到毕业的总时间：天数
        if self.role == 1:
            year = str(int(self.number[0:4]) + 4)
            future = datetime.strptime(year + '-6-1 0:0:0', '%Y-%m-%d %H:%M:%S')
            now = datetime.now()  # 当前时间
            delta = future - now  # 求时间差
            self.studyDays = delta.days

    def delete_plans(self):
        if self.plans:
            for plan in self.plans:
                db.session.delete(plan)
            db.session.commit()


# 加载用户的回调函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


