from app import db
from datetime import date


class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    beginTime = db.Column(db.Date)  # 理想开始计划时间
    endTime = db.Column(db.Date)  # 理想结束计划时间
    actualEndTime = db.Column(db.Date)  # 实际结束计划时间
    days = db.Column(db.Integer)  # 理想计划执行天数
    state = db.Column(db.Integer, default=0)  # 标记计划状态，0：未完成   1：已完成    2：正在进行

    directionDetailId = db.Column(db.Integer, db.ForeignKey('directionDetail.id'))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', back_populates='plans')
    directionDetail = db.relationship('DirectionDetail')

    def __repr__(self):
        return '<plan user:%r directionDetail:%r>' % self.user.username, self.directionDetail.name

    def __setstate__(self, state):
        if state == 1:
            self.state = state
            self.actualEndTime = date.today()
        if state == 2:
            self.state = state

    def set_actual_end_time(self, year, month, day):
        appoint_date = date(year=year, month=month, day=day)
        self.actualEndTime = appoint_date
