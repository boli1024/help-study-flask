from app import db


class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    cycle = db.Column(db.Integer)
