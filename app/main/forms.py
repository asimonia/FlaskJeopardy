from flask.ext.wtf import Form
from wtforms import SelectField, StringField, IntegerField, SubmitField
from wtforms.validators import Required

class GameForm(Form):
	players = SelectField('How many players?', choices=[(1, "One Player"), (2, "Two Players"), (3, "Three Players")], coerce=int)
	playerone_name = StringField('Name of Player 1', validators=[Required()])
	playertwo_name = StringField('Name of Player 2', validators=[Required()])
	playerthree_name = StringField('Name of Player 3', validators=[Required()])
	show_number = IntegerField('Choose show number', validators=[Required()])
	submit = SubmitField('Start')
