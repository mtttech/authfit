import customtkinter

from assets import ExerciseDatabase

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


db = ExerciseDatabase()


class ExerciseInfoBox(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=400)
        # Type Label
        self.label_type = customtkinter.CTkLabel(self, text="Type")
        self.label_type.grid(row=0, column=0)
        # Type Entry
        self.label_type_entry = customtkinter.CTkEntry(
            self, width=400, state="disabled"
        )
        self.label_type_entry.grid(row=1, column=0)
        # Muscle Label
        self.label_muscle = customtkinter.CTkLabel(self, text="Muscle")
        self.label_muscle.grid(row=2, column=0)
        # Muscle Entry
        self.label_muscle_entry = customtkinter.CTkEntry(
            self, width=400, state="disabled"
        )
        self.label_muscle_entry.grid(row=3, column=0)
        # Equipment Label
        self.label_equip = customtkinter.CTkLabel(self, text="Equipment")
        self.label_equip.grid(row=4, column=0)
        # Equipment Entry
        self.label_equip_entry = customtkinter.CTkEntry(
            self, width=400, state="disabled"
        )
        self.label_equip_entry.grid(row=5, column=0)
        # Difficulty Label
        self.label_difficulty = customtkinter.CTkLabel(self, text="Difficulty")
        self.label_difficulty.grid(row=6, column=0)
        # Difficulty Entry
        self.label_difficulty_entry = customtkinter.CTkEntry(
            self, width=400, state="disabled"
        )
        self.label_difficulty_entry.grid(row=7, column=0)
        # Infobox Label
        self.label_infobox = customtkinter.CTkLabel(self, text="Instruction")
        self.label_infobox.grid(row=8, column=0)
        # Infobox Textbox
        self.textbox_infobox = customtkinter.CTkTextbox(
            self, width=400, state="disabled"
        )
        self.textbox_infobox.grid(row=9, column=0, sticky="nsew")


class Authenticity(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Authenticity Fitness App")
        self.geometry("1100x580")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        muscles_worked_list = db.get_muscles_worked_list()
        muscles_worked_list = [m[0] for m in muscles_worked_list]

        # Start main frame window.
        self.selector_frame = customtkinter.CTkFrame(self, width=1100)

        # Muscle Group Label
        self.muscle_selector_label = customtkinter.CTkLabel(
            self.selector_frame, text="Muscle Group"
        )
        self.muscle_selector_label.grid(row=0, column=0, padx=0, pady=0)
        # Exercise Group Label
        self.muscle_selector_label = customtkinter.CTkLabel(
            self.selector_frame, text="Exercises"
        )
        self.muscle_selector_label.grid(row=0, column=1, padx=0, pady=0)

        # Muscle Group Option Menu
        self.muscle_selector_optionemenu = customtkinter.CTkOptionMenu(
            self.selector_frame,
            values=muscles_worked_list,
            width=300,
            command=self.activate_exercise_option_menu,
            anchor="center",
        )
        self.muscle_selector_optionemenu.grid(row=1, column=0, padx=20, pady=20)
        # Exercise Group Option Menu
        self.exercise_selector_optionemenu = customtkinter.CTkOptionMenu(
            self.selector_frame,
            values=["Select Muscle Group"],
            width=300,
            state="disabled",
            anchor="center",
        )
        self.exercise_selector_optionemenu.grid(row=1, column=1, padx=20, pady=20)
        # Exercise Info Box
        self.info_frame = ExerciseInfoBox(self.selector_frame)
        self.info_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # End main frame window.
        self.selector_frame.grid(row=0, column=0, padx=0)

    def activate_exercise_option_menu(self, choice):
        exercises_by_muscle_list = db.get_exercises_by_muscle_list(choice)
        exercises_by_muscle_list = [e[1] for e in exercises_by_muscle_list]
        self.exercise_selector_optionemenu.configure(
            state="normal", values=exercises_by_muscle_list
        )
        self.exercise_selector_optionemenu.set(exercises_by_muscle_list[0])


def main():
    app = Authenticity()
    app.mainloop()


if __name__ == "__main__":
    main()
