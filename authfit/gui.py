import datetime

import customtkinter

from authfit.assets import ExerciseDatabase


def change_widget_state(widget, index, value) -> None:
    widget.configure(state="normal")
    widget.delete(index, "end")
    widget.insert(index, value)
    widget.configure(state="disabled")


class _AFEntry(customtkinter.CTkEntry):
    def __init__(self, master, width):
        super().__init__(master, border_width=1, fg_color="#eeeeee", width=width)


class AFMainWindow(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Authenticity Fitness")
        height, width = (655, 392)
        self.geometry(f"{width}x{height}")
        self.maxsize(width, height)
        self.create_window()

    def create_window(self) -> None:
        tabview = AFTabview(self)
        tabview.grid(column=0, row=0, padx=5, pady=5)


class AFTabview(customtkinter.CTkTabview):
    def __init__(self, master) -> None:
        super().__init__(master, height=600, width=350)

        self.add("Tracker")
        self.add("Database")
        self.set("Tracker")

        tracker = AFTracker(self.tab("Tracker"))
        tracker.grid(column=0, row=0)

        database = AFDatabase(self.tab("Database"))
        database.grid(column=0, row=0)


class AFTracker(customtkinter.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master, height=600, width=350)

        workout_title = customtkinter.CTkEntry(
            self,
            border_width=1,
            fg_color="transparent",
            font=("Arial", 34),
            placeholder_text="Workout Name...",
            width=330,
        )
        workout_title.grid(column=0, row=0, padx=20, pady=10)

        timer = customtkinter.CTkLabel(self, text="timer")
        timer.grid(column=0, row=1)

        wt = WorkoutTable(self, "Deadlift")
        wt.grid(column=0, row=3, padx=10, pady=10)


class WorkoutTable(customtkinter.CTkScrollableFrame):
    def __init__(self, master, label):
        super().__init__(
            master, corner_radius=30, fg_color="#eeeeee", height=400, width=300
        )

        add_exercise = customtkinter.CTkButton(self, text="Add Exercise")

        exercise_lbl = customtkinter.CTkLabel(self, text=label)

        workout_notes = customtkinter.CTkTextbox(
            self,
            border_width=1,
            fg_color="transparent",
            height=50,
            width=250,
        )

        lbl_set = customtkinter.CTkLabel(self, text="Set", width=40)
        set_btn1 = customtkinter.CTkButton(self, text="1", width=40)
        set_btn2 = customtkinter.CTkButton(self, text="2", width=40)
        set_btn3 = customtkinter.CTkButton(self, text="3", width=40)
        set_btn4 = customtkinter.CTkButton(self, text="4", width=40)

        lbl_wgt = customtkinter.CTkLabel(self, text="Wgt. (kg)")
        wgt_ety1 = _AFEntry(self, 40)
        wgt_ety2 = _AFEntry(self, 40)
        wgt_ety3 = _AFEntry(self, 40)
        wgt_ety4 = _AFEntry(self, 40)

        lbl_reps = customtkinter.CTkLabel(self, text="Reps", width=30)
        rep_ety1 = _AFEntry(self, 30)
        rep_ety2 = _AFEntry(self, 30)
        rep_ety3 = _AFEntry(self, 30)
        rep_ety4 = _AFEntry(self, 30)

        add_exercise.grid(column=0, columnspan=3, row=0, padx=20, pady=20)
        exercise_lbl.grid(column=0, columnspan=3, row=1, padx=5, pady=5)
        workout_notes.grid(column=0, columnspan=3, row=2, padx=20, pady=10)
        workout_notes.insert("0.0", "Notes...")

        lbl_set.grid(column=0, row=3, padx=5, pady=5)
        set_btn1.grid(column=0, row=4, padx=5, pady=5)
        set_btn2.grid(column=0, row=5, padx=5, pady=5)
        set_btn3.grid(column=0, row=6, padx=5, pady=5)
        set_btn4.grid(column=0, row=7, padx=5, pady=5)

        lbl_wgt.grid(column=1, row=3, padx=5, pady=5)
        wgt_ety1.grid(column=1, row=4, padx=5, pady=5)
        wgt_ety2.grid(column=1, row=5, padx=5, pady=5)
        wgt_ety3.grid(column=1, row=6, padx=5, pady=5)
        wgt_ety4.grid(column=1, row=7, padx=5, pady=5)

        lbl_reps.grid(column=2, row=3, padx=5, pady=5)
        rep_ety1.grid(column=2, row=4, padx=5, pady=5)
        rep_ety2.grid(column=2, row=5, padx=5, pady=5)
        rep_ety3.grid(column=2, row=6, padx=5, pady=5)
        rep_ety4.grid(column=2, row=7, padx=5, pady=5)


class AFDatabase(customtkinter.CTkFrame):
    DB_EXERCISES = ExerciseDatabase()
    MUSCLES_WORKED_OPTIONS = [m[0] for m in DB_EXERCISES.get_muscles_worked_list()]
    LABEL_WIDGET_WIDTH = 180
    OPTMENU_WIDGET_WIDTH = 350

    def __init__(self, master) -> None:
        super().__init__(master, height=600, width=350)

        group_selector = customtkinter.CTkOptionMenu(
            self,
            values=self.MUSCLES_WORKED_OPTIONS,
            width=self.OPTMENU_WIDGET_WIDTH,
            command=self._activate_selector,
            anchor="center",
        )
        self.exercise_selector = customtkinter.CTkOptionMenu(
            self,
            values=["Select Muscle Group"],
            width=self.OPTMENU_WIDGET_WIDTH,
            state="disabled",
            command=self._fill_exercise_info_box,
            anchor="center",
        )
        self.textbox_infobox = customtkinter.CTkTextbox(
            self,
            fg_color="transparent",
            height=450,
            width=330,
            state="disabled",
            text_color="#808080",
            wrap="word",
        )

        group_selector.grid(column=0, row=0, padx=10, pady=10)
        self.exercise_selector.grid(column=0, row=1, padx=10, pady=10)
        self.textbox_infobox.grid(column=0, row=2, padx=10, pady=10)

    def _activate_selector(self, choice) -> None:
        exercises_by_muscle_list = self.DB_EXERCISES.get_exercises_by_muscle_list(
            choice
        )
        exercises_by_muscle_list = [e[0] for e in exercises_by_muscle_list]
        self.exercise_selector.configure(
            state="normal", values=exercises_by_muscle_list
        )
        self.exercise_selector.set(exercises_by_muscle_list[0])

    def _fill_exercise_info_box(self, choice) -> None:
        (
            exercise_type,
            equipment,
            difficulty,
            instructions,
        ) = self.DB_EXERCISES.get_exercise_entry(choice)[0]
        # Exercise instructions
        change_widget_state(self.textbox_infobox, 1.0, instructions)
