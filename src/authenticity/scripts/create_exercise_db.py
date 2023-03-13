"""
lats
lower_back
middle_back
neck
quadriceps
traps
triceps
"""
import json
import os
import sqlite3

import requests


def get_exercise_json_payload(out):
    return [tuple(dict(e).values()) for e in json.loads(out.strip())]


APP_DIR = os.path.dirname(__file__)
EXERCISE_DATABASE = os.path.join(APP_DIR, "assets/exercises.db")

conn = sqlite3.connect(EXERCISE_DATABASE)
curs = conn.cursor()

for muscle in ("glutes", "hamstrings"):
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
