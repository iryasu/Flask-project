from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, 
                    DateTimeField, RadioField, 
                    SelectField, TextAreaField, SubmitField )
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secKey1'

class InfoForm(FlaskForm):
    
    breed = StringField("What breed are you ?", validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered ?")
    mood = RadioField('Please choose your mood',
                        choices = [('mood_one','happy'),
                                    ('mood_two','Excited'),
                                    ('mood_three', 'Hungry')])
    food_choice = SelectField(u'Pick your favourite food: ',
                            choices = [('chick','chicken'),
                                        ('bf', 'beef'),
                                        ('fish','fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        flash('thank you for filling the form !')   ## creates an alert box

        session['fields'] = ['breed', 'neutered', 'mood', 'food', 'feedback']
        session['breed'] = form.breed.data                      ## store data for a user session
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        
        return redirect(url_for('thank_you'))                   ## redirect user when he submits
    return render_template('index.html', form=form)             ## render page first time

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')



if __name__ == '__main__':
    app.run(debug=True)