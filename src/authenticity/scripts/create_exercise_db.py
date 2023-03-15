import json
import os
from pathlib import Path
import sqlite3

import requests


APP_DIR = os.path.dirname(__file__)
EXERCISE_DATABASE = Path(APP_DIR).parent / "assets/exercises.db"

conn = sqlite3.connect(EXERCISE_DATABASE)
curs = conn.cursor()


def get_exercise_json_payload(out):
    return [tuple(dict(e).values()) for e in json.loads(out.strip())]


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

for muscle in (
    "lats",
    "lower_back",
    "middle_back",
    "neck",
    "quadriceps",
    "traps",
    "triceps",
):
    api_url = "https://api.api-ninjas.com/v1/exercises?muscle={}".format(muscle)
    response = requests.get(
        api_url, headers={"X-Api-Key": "EUkhC02XAhP6mI+RdxAzWA==L1mQza6laXxzy97V"}
    )
    if response.status_code == requests.codes.ok:
        for exercise_row in get_exercise_json_payload(response.text):
            curs.execute(
                "INSERT INTO exercises (name, type, muscle, equipment, difficulty, instructions) VALUES(?,?,?,?,?,?)",
                exercise_row,
            )
            conn.commit()
    else:
        print("Error:", response.status_code, response.text)
