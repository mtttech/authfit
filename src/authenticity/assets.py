import os
import sqlite3


class AuthenticityExerciseDB:
    EXERCISE_DATABASE = os.path.join(os.path.dirname(__file__), "assets/exercises.db")

    def __init__(self):
        conn = sqlite3.connect(self.EXERCISE_DATABASE)
        self.curs = conn.cursor()

    def get_muscles_worked_list(self):
        self.curs.execute("SELECT DISTINCT muscle FROM exercises")
        return self.curs.fetchall()
    
    def get_exercises(self):
        self.curs.execute("SELECT EID, name FROM exercises")
        return self.curs.fetchall()
