from datetime import datetime
from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=True)
    creation_date = \
        db.Column(db.TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, nullable=False)
    tag_id = db.Column(db.Integer, nullable=True)

    @property
    def tag(self):
        if self.tag_id:
            return Tags.query.filter_by(id=self.tag_id).first().name
        return ""

    def __repr__(self):
        return '<User %r>' % self.title
