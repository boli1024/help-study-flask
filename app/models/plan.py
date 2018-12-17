from app import db


class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    beginTime = db.Column(db.Date)
    endTime = db.Column(db.Date)
    days = db.Column(db.Integer)
    state = db.Column(db.Integer, default=0)  # 标记计划状态，0：未完成   1：已完成    2：正在进行

    directionDetailId = db.Column(db.Integer, db.ForeignKey('directionDetail.id'))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', back_populates='plans')
    directionDetail = db.relationship('DirectionDetail')

    def __repr__(self):
        return '<plan user:%r directionDetail:%r>' % self.user.username, self.directionDetail.name
