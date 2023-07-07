import os
import sqlite3


class AuthenticityDatabase:
    def __init__(self) -> None:
        self.db_path = os.path.join(os.path.dirname(__file__), "assets/exercises.db")

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()
        return cursor

    def __exit__(self, _type, value, traceback):
        self.conn.close()


def get_exercise_entry(name) -> list:
    with AuthenticityDatabase() as cursor:
        result = cursor.execute(
            "SELECT type, equipment, difficulty, instructions FROM exercises WHERE name=?",
            (name,),
        )
        return result.fetchall()


def get_exercises_by_group(muscle: str) -> list:
    with AuthenticityDatabase() as cursor:
        result = cursor.execute(
            "SELECT name FROM exercises WHERE muscle=? ORDER BY name", (muscle,)
        )
        return result.fetchall()
    

def get_muscle_groups() -> list:
    with AuthenticityDatabase() as cursor:
        result = cursor.execute("SELECT DISTINCT muscle FROM exercises")
        return result.fetchall()
