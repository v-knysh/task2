import re

from sqlalchemy.orm import validates

from app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    @validates('name')
    def validate_name(self, key, value):
        if not (value and re.match(r"^\w{3,30}$", value)):
            raise ValueError('validation error')
        if Person.query.filter_by(name=value).all():
            raise ValueError(f'name {value} already exists')
        return value

    def __str__(self):
        return self.name
