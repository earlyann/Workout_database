CREATE TABLE "workout" (
    "user_id" INT  NOT NULL,
    "exercise_id" INT   NOT NULL,
    "workout_date" DATE   NOT NULL
);

CREATE TABLE "movement" (
    "movement_id" SERIAL NOT NULL,
    "name" VARCHAR   NOT NULL,
    "description" VARCHAR   NOT NULL,
    "primary_muscle_group" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Movement" PRIMARY KEY (
        "movement_id"
     )
);

CREATE TABLE "user" (
    "user_id"  SERIAL NOT NULL,
    "user_name" VARCHAR   NOT NULL,
    "password" VARCHAR(18)   NOT NULL,
    CONSTRAINT "pk_User" PRIMARY KEY (
        "user_id"
     )
);

CREATE TABLE "exercise" (
    "exercise_id" SERIAL NOT NULL,
    "movement_id" INT   NOT NULL,
    "number_of_sets" INT   NOT NULL,
    "number_of_reps" INT   NOT NULL,
    "time" INTERVAL MINUTE TO SECOND NOT NULL,
    CONSTRAINT "pk_Exercise" PRIMARY KEY (
        "exercise_id"
     )
);

ALTER TABLE "workout" ADD CONSTRAINT "fk_workout_user_id" FOREIGN KEY("user_id")
REFERENCES "user" ("user_id");

ALTER TABLE "workout" ADD CONSTRAINT "fk_workout_exercise_id" FOREIGN KEY("exercise_id")
REFERENCES "exercise" ("exercise_id");

ALTER TABLE "exercise" ADD CONSTRAINT "fk_Exercise_movement_id" FOREIGN KEY("movement_id")
REFERENCES "movement" ("movement_id");

ALTER TABLE "exercise"
ADD CONSTRAINT "positive_sets" CHECK ("number_of_sets" > 0);

ALTER TABLE "exercise" 
ADD CONSTRAINT "positive_reps" CHECK ("number_of_reps" > 0);

INSERT INTO movement (name, description, primary_muscle_group)
VALUES ('Dumbbell Clean', 'Standing over the DB, snap to the rack', 'Arms'),
       ('Single Arm Dumbbell Press', 'With one arm, starting in the rack press up', 'Arms'),
       ('Double Dumbbell Pres', 'With two DBs, starting in the rack press up', 'Arms'),
       ('Sumo Kettlebell Deadlift', 'Start standing wide in front of two KBs on the ground, pick it up', 'Back'),
       ('Kettlebell Deadlift', 'Start standing in front of two KBs, pick it up', 'Back');


INSERT INTO "user" (user_name, password)
VALUES ('testuser', 'bike123');
 
ALTER TABLE "user" RENAME TO "users";

SELECT * FROM "user";

