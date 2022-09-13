from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length


class TVShowForm(FlaskForm):
    name = StringField('Movie Name', validators=[DataRequired(), Length(min=2, max=120)])
    director = StringField('Director')
    no_of_episodes = StringField('No of episodes')
    released_year = DateTimeField('released_year')
    end_date = DateTimeField('released_year')
    genre = StringField('released_year')


class CarForm(FlaskForm):
    name = StringField('Car Name', validators=[DataRequired(), Length(min=2, max=120)])
    brand = StringField('Brand')
    seating_capacity = StringField('Seating Capacity')
    model_released_year = DateTimeField('model_released_year')
    type = StringField('type')