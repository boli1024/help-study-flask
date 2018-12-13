from app import db


class Direction(db.Model):
    __tablename__ = 'direction'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    content = db.Column(db.Text, nullable=False)

    users = db.relationship('User', backref='direction', lazy='dynamic')
    courses = db.relationship('Course', backref='direction', lazy='dynamic')

    def __repr__(self):
        return '<direction %r>' % self.name
