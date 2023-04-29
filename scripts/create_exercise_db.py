import json
import os
from pathlib import Path
import sqlite3

import requests


API_KEY = "Enter API Ninjas' Key Here"
APP_DIR = os.path.dirname(__file__)
EXERCISE_DATABASE = Path(APP_DIR).parent / "authfit/assets/exercises.db"


def get_exercise_rows(json_payload: str) -> list:
    """Prepares json payload for database insertion."""
    return [tuple(dict(e).values()) for e in json.loads(json_payload.strip())]


def main() -> None:
    conn = sqlite3.connect(EXERCISE_DATABASE)
    curs = conn.cursor()
    curs.execute('''
        CREATE TABLE IF NOT EXISTS exercises
        (name TEXT,
        type TEXT,
        muscle TEXT,
        equipment TEXT,
        difficulty TEXT,
        instructions TEXT)
        ''')
    conn.commit()

    muscle_groups = (
        "abdominals",
        "abductors",
        "adductors",
        "biceps",
        "calves",
        "chest",
        "forearms",
        "glutes",
        "hamstrings",
        "lats",
        "lower_back",
        "middle_back",
        "neck",
        "quadriceps",
        "traps",
        "triceps",
    )

    for muscle in muscle_groups:
        api_url = "https://api.api-ninjas.com/v1/exercises?muscle={}".format(muscle)
        response = requests.get(
            api_url, headers={"X-Api-Key": API_KEY}
        )
        if response.status_code != requests.codes.ok:
            print("Error:", response.status_code, response.text)
            continue
        
        json_payload = get_exercise_rows(response.text)
        if len(json_payload) == 0:
            print("Error: json payload empty. Skipping...")
            continue

        for exercise_row in json_payload:
            curs.execute(
                '''
                INSERT INTO exercises 
                (name, type, muscle, equipment, difficulty, instructions) 
                VALUES(?,?,?,?,?,?)
                ''',
                exercise_row,
            )
            conn.commit()

    conn.close()


if __name__ == "__main__":
    main()
