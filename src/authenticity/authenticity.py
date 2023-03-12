from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Header, Footer, Static

from assets import AuthenticityExerciseDB


db = AuthenticityExerciseDB()


class MusclesWorkedSelector(Static):

    def compose(self) -> ComposeResult:
        for row in db.get_muscles_worked_list():
            yield Button(row[0], id=row[0])


class ExerciseSelector(Static):

    def compose(self) -> ComposeResult:
        for row in db.get_exercises():
            yield Button(row[1], id=row[1])


class AuthenticityApp(App):

    CSS_PATH = "authenticity.css"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(MusclesWorkedSelector(), ExerciseSelector())
        yield Footer()


def main():
    print("Authenticity App main.")
    app = AuthenticityApp()
    app.run()


if __name__ == "__main__":
    main()
