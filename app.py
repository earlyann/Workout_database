from flask import Flask, render_template, request, redirect, url_for, make_response
from forms import ExerciseForm,NewWorkoutForm
from flask_sqlalchemy import SQLAlchemy

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lift123$'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5433/workout_log'


db = SQLAlchemy(app)

# This class wasn't coming over with the autobase
class Workout(db.Model):
    __tablename__ = 'workouts'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.exercise_id'), primary_key=True)
    workout_date = db.Column(db.Date, nullable=False)

    user = db.relationship('User', backref='workouts')
    exercise = db.relationship('Exercise', backref='workouts')
    
Base = automap_base()

# Wrap this code inside app.app_context()
with app.app_context():
    engine = create_engine('postgresql://postgres:postgres@localhost:5433/workout_log')
    Base.prepare(autoload_with=engine)

    Movement = Base.classes.movement
    User = Base.classes.users
    Exercise = Base.classes.exercise


# Defining the index route, including a list all the available routes.
@app.route("/")
def home():
    with app.app_context():
        response = make_response(f"LACEY'S WORKOUT LOG /new-workout)
        response.headers = [('Content-Type', 'text/plain')]
        return response

@app.route('/new-workout', methods=['GET', 'POST'])
def new_workout():
    with app.app_context():
        form = NewWorkoutForm()
        if request.method == 'POST' and form.validate():
            username = form.username.data
            session = Session(db.engine)
            user = session.query(User).filter_by(username=username).first()
            if not user:
                flash('Invalid username')
                return redirect(url_for('new_workout', username=username))

            # Create a new Workout object and associate it with each Exercise object
            workout = Workout(user_id=user.user_id, date=form.date.data)
            session.add(workout)
            session.commit()

            for exercise_form in form.exercises:
                movement = session.query(Movement).filter_by(name=exercise_form.movement.data).first()
                if not movement:
                    movement = Movement(name=exercise_form.movement.data,
                                        description='',
                                        primary_muscle_group='')
                    session.add(movement)
                    session.commit()

                exercise = Exercise(workout_id=workout.workout_id,
                                    movement_id=movement.movement_id,
                                    sets=exercise_form.sets.data,
                                    reps=exercise_form.reps.data,
                                    weight=exercise_form.weight.data,
                                    time=exercise_form.time.data,
                                    date=form.date.data)
                session.add(exercise)
                session.commit()

            return redirect(url_for('home'))
        return render_template('new_workout.html', form=form, users=db.session.query(User).all())



if __name__ == '__main__':
    with app.app_context():
        # Move this line inside a request context
        db.create_all()
        
    app.run(debug=True)

