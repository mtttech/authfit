import os

import customtkinter

from .gui import AuthenticityMainWindow


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class Authenticity(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Authenticity Fitness")
        self.geometry("800x605")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Authenticity Main Window.
        self.main_window = customtkinter.CTkFrame(self)
        self.main_window.grid(row=0, column=0, padx=0, sticky="nsew")
        # Authenticity App Window
        self.app_window = AuthenticityMainWindow(self.main_window)
        self.app_window.grid(row=0, column=0)


def main() -> None:
    app_dir = os.path.dirname(__file__)
    exercises_db = os.path.join(app_dir, 'assets/exercises.db')
    try:
        if not os.path.isfile(exercises_db):
            raise RuntimeError(f"Exercises database '{exercises_db}' exists: NOT OK")
    except RuntimeError as e:
        print(e)
        exit(1)
    finally:
        print(f"Exercises database '{exercises_db}' exists: OK")
        app = Authenticity()
        app.mainloop()


if __name__ == "__main__":
    main()