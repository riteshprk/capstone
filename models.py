import os
import json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#database_name = "capstone"
#database_path = os.environ['DATABASE_URL']
database_path = "postgres://vszpbdrdkjpqmr:caaa62f039d2f3892b767609804e269e43ef0ea2e2494f62ceed8ca48beded6f@ec2-54-75-246-118.eu-west-1.compute.amazonaws.com:5432/d9of6292e5hv5f"

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
   # db.create_all()  # 'use migrate


'''
Actor

'''


class Actor(db.Model):
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,  unique=True, nullable=False)
    age = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }


'''
Movie

'''


class Movie(db.Model):
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String,  unique=True, nullable=False)
    release_date = db.Column(db.Date, nullable=True)
    actors = db.relationship('Actor', secondary='relation', lazy='subquery',
                             backref=db.backref('movies', lazy=True))

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }


relation = db.Table('relation',
                    db.Column('actor_id', db.Integer, db.ForeignKey(
                        'Actor.id'), primary_key=True),
                    db.Column('movie_id', db.Integer, db.ForeignKey(
                        'Movie.id'), primary_key=True)
                    )
