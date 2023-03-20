import customtkinter

from .assets import ExerciseDatabase
from .widgets import ExerciseInfoBox

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


DB_EXERCISES = ExerciseDatabase()


class Authenticity(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Authenticity Fitness App")
        self.geometry("1100x640")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        muscles_worked_list = DB_EXERCISES.get_muscles_worked_list()
        muscles_worked_list = [m[0] for m in muscles_worked_list]

        # Start main frame window.
        self.main_window = customtkinter.CTkFrame(self)
        # Muscle Group Label
        self.muscle_selector_label = customtkinter.CTkLabel(
            self.main_window, text="Muscle Group"
        )
        self.muscle_selector_label.grid(row=0, column=0, padx=0, pady=(20, 0))
        # Muscle Group Option Menu
        self.muscle_selector_optionemenu = customtkinter.CTkOptionMenu(
            self.main_window,
            values=muscles_worked_list,
            width=300,
            command=self._activate_exercise_option_menu,
            anchor="center",
        )
        self.muscle_selector_optionemenu.grid(row=1, column=0, padx=0, pady=0)
        # Exercise Group Label
        self.muscle_selector_label = customtkinter.CTkLabel(
            self.main_window, text="Exercises"
        )
        self.muscle_selector_label.grid(row=2, column=0, padx=0, pady=0)
        # Exercise Group Option Menu
        self.exercise_selector_optionemenu = customtkinter.CTkOptionMenu(
            self.main_window,
            values=["Select Muscle Group"],
            width=300,
            state="disabled",
            command=self._fill_exercise_info_box,
            anchor="center",
        )
        self.exercise_selector_optionemenu.grid(row=3, column=0, padx=0, pady=0)
        # Exercise Info Box
        self.infobox_frame = ExerciseInfoBox(self.main_window)
        self.infobox_frame.grid(row=4, column=0, padx=15, pady=(30, 20))
        # End main frame window.
        self.main_window.grid(row=0, column=0, padx=0, sticky="nsew")

    def _activate_exercise_option_menu(self, choice) -> None:
        exercises_by_muscle_list = DB_EXERCISES.get_exercises_by_muscle_list(choice)
        exercises_by_muscle_list = [e[1] for e in exercises_by_muscle_list]
        self.exercise_selector_optionemenu.configure(
            state="normal", values=exercises_by_muscle_list
        )
        self.exercise_selector_optionemenu.set(exercises_by_muscle_list[0])

    @staticmethod
    def _change_disabled_input_value(widget, index, value) -> None:
        widget.configure(state="normal")
        widget.delete(index, "end")
        widget.insert(index, value)
        widget.configure(state="disabled")

    def _fill_exercise_info_box(self, choice) -> None:
        exercise_type, equipment, difficulty, instructions = DB_EXERCISES.get_exercise_entry(
            choice
        )[0]
        # Exercise type
        Authenticity._change_disabled_input_value(
            self.infobox_frame.label_type_entry, 0, exercise_type
        )
        # Exercise equipment
        Authenticity._change_disabled_input_value(
            self.infobox_frame.label_equip_entry, 0, equipment
        )
        # Exercise difficulty
        Authenticity._change_disabled_input_value(
            self.infobox_frame.label_difficulty_entry, 0, difficulty
        )
        # Exercise instructions
        Authenticity._change_disabled_input_value(
            self.infobox_frame.textbox_infobox, 1.0, instructions
        )


def main():
    app = Authenticity()
    app.mainloop()


if __name__ == "__main__":
    main()
