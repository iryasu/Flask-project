import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
#__file__ is the current file and dirname returns its path

app = Flask(__name__)

############################     CREATING DATABASE ############################
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)


##############################################################################

class Puppy(db.Model):

    # Overriding the table name manually
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Puppy {self.name} is {self.age} years old'