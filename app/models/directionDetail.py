from app import db


class DirectionDetail(db.Model):
    __tablename__ = 'directionDetail'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    direction_id = db.Column(db.Integer, db.ForeignKey('direction.id'))

    direction = db.relationship('Direction', back_populates='details')
    # plans = db.relationship('Plan', back_populates='directionDetail')

    def __repr__(self):
        return '<plan name:%r weight:%d>' % self.name, self.weight


if __name__ == '__main__':
    detail = DirectionDetail(1, 'test', '20')
