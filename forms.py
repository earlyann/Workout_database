from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_wtf.file import FileField, FileRequired
from flask_wtf.recaptcha import RecaptchaField
from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class ExerciseForm(FlaskForm):
    movement = StringField('Movement', validators=[DataRequired(), Length(max=100)])
    sets = IntegerField('Sets', validators=[DataRequired()])
    reps = IntegerField('Reps', validators=[DataRequired()])
    weight = IntegerField('Weight', validators=[DataRequired()])
    time = StringField('Time', validators=[DataRequired(), Length(max=8)])

class NewWorkoutForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    exercises = FieldList(FormField(ExerciseForm), min_entries=1)
    date = DateField('Date', validators=[DataRequired()])
    add_exercise = SubmitField('Add Exercise')
    submit = SubmitField('Submit')


