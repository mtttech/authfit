import os
import sqlite3


class ExerciseDatabase:
    EXERCISE_DATABASE = os.path.join(os.path.dirname(__file__), "assets/exercises.db")

    def __init__(self):
        conn = sqlite3.connect(self.EXERCISE_DATABASE)
        self.curs = conn.cursor()

    def get_muscles_worked_list(self):
        self.curs.execute("SELECT DISTINCT muscle FROM exercises")
        return self.curs.fetchall()

    def get_exercises_by_muscle_list(self, muscle):
        self.curs.execute(
            "SELECT EID, name FROM exercises WHERE muscle=? ORDER BY name", (muscle,)
        )
        return self.curs.fetchall()

    def get_exercise_entry(self, name):
        self.curs.execute(
            "SELECT type, equipment, difficulty, instructions FROM exercises WHERE name=?",
            (name,),
        )
        return self.curs.fetchall()