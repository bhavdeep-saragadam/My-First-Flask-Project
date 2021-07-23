from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, 
BooleanField, 
DateTimeField, 
RadioField, 
SelectField, 
TextAreaField, 
TextField, 
SubmitField)
from wtforms.validators import DataRequired


app = Flask(__name__)




app.config['SECRET_KEY'] = '12345'


class InfoForm(FlaskForm):
	breed = StringField('What Breed Are You?: ', validators=[DataRequired()])
	mood = RadioField('Please Choose Your Mood: ',
	choices = [
		('mood_one','Happy',),
		('mood_two','Excited')
		])

	food_choices = SelectField(u'Pick Your Favorite Food: ',
	
	choices = [
		('chi','Chicken'),
		('fish','Fish')
	])

	feedback = TextAreaField()
	submit = SubmitField()



@app.route('/', methods=['GET', 'POST'])
def index():

	form = InfoForm()

	if form.validate_on_submit():
		session['breed'] = form.breed.data
		session['mood'] = form.mood.data
		session['food'] = form.food_choices.data
		session['feedback'] = form.feedback.data
		
		return redirect(url_for('thankyou'))
	return render_template('index.html', form=form)

@app.route('/thankyou')
def thankyou():
	return render_template('thank-you.html')

if __name__ == '__main__':
	app.run(debug=True)