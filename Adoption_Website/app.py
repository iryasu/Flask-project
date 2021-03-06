# app.py
import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm, DelForm, AddOwner


############################     CREATING APP AND DATABASE ############################
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)
##########################################


class Puppy(db.Model):
    __tablename__='puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'Puppy name is : {self.name}'


class Owner(db.Model):
    __tablename__='owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id


################ VIEW FUNCTIONS

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pup'))    
    return render_template('add.html', form=form)

@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=['GET', 'POST'])
def delete_pup():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data

        pup_to_del = Puppy.query.get(id)
        db.session.delete(pup_to_del)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)

@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():

    form = AddOwner()

    if form.validate_on_submit():

        name = form.name.data
        pup_id = form.id.data

        owner = Owner(name, pup_id)
        db.session.add(owner)
        db.session.commit()
        return redirect(url_for('list_pup'))    
    return render_template('addOwner.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)