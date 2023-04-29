import os

import customtkinter
from rich import print

from .gui import AFMainWindow


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def main() -> None:
    app_dir = os.path.dirname(__file__)
    exercises_db = os.path.join(app_dir, "assets/exercises.db")

    try:
        if not os.path.isfile(exercises_db):
            print(
                f"Exercise database '{exercises_db}' exists: [bold][red]NOT OK[/red][/bold]"
            )
            raise RuntimeError
    except RuntimeError:
        exit(1)
    else:
        print(
            f"Exercise database '{exercises_db}' exists: [bold][green]OK[/green][/bold]"
        )
        app = AFMainWindow()
        app.mainloop()


if __name__ == "__main__":
    main()
