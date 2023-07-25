from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, AnyOf

class RandomFactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    birth_year = StringField("Birth Year", validators=[InputRequired(), NumberRange(1900,2000,message="Year must be within 1900 and 2000") ])
    color = StringField("Color", validators=[AnyOf(values=['blue', 'green', 'orange', 'red'], message="Must be one of these: blue, green, red, orange")])