import datetime

import customtkinter

from .assets import ExerciseDatabase


class AuthenticityMainWindow(customtkinter.CTkFrame):
    DB_EXERCISES = ExerciseDatabase()
    MUSCLES_WORKED_OPTIONS = [m[0] for m in DB_EXERCISES.get_muscles_worked_list()]
    INPUT_WIDGET_WIDTH = 400

    def __init__(self, master):
        super().__init__(master, width=self.INPUT_WIDGET_WIDTH)
        # Muscle Group Label
        self.muscle_selector_label = customtkinter.CTkLabel(self, text="Muscle Group")
        self.muscle_selector_label.grid(row=0, column=0, padx=0, pady=(20, 0))
        # Muscle Group Option Menu
        self.muscle_selector_optionemenu = customtkinter.CTkOptionMenu(
            self,
            values=self.MUSCLES_WORKED_OPTIONS,
            width=300,
            command=self._activate_exercise_option_menu,
            anchor="center",
        )
        self.muscle_selector_optionemenu.grid(row=1, column=0, padx=0, pady=0)
        # Exercise Group Label
        self.muscle_selector_label = customtkinter.CTkLabel(self, text="Exercises")
        self.muscle_selector_label.grid(row=2, column=0, padx=0, pady=0)
        # Exercise Group Option Menu
        self.exercise_selector_optionemenu = customtkinter.CTkOptionMenu(
            self,
            values=["Select Muscle Group"],
            width=300,
            state="disabled",
            command=self._fill_exercise_info_box,
            anchor="center",
        )
        self.exercise_selector_optionemenu.grid(row=3, column=0, padx=0, pady=0)
        # Exercise Info Box
        self.infobox_frame = _ExerciseInfoBox(self)
        self.infobox_frame.grid(row=4, column=0, padx=15, pady=(30, 20))

        ## COL 2
        self.workout_calender = _WorkoutCalender(self)
        self.workout_calender.grid(row=0, column=1, rowspan=5, padx=0, pady=0, sticky="nsew")

    def _activate_exercise_option_menu(self, choice) -> None:
        exercises_by_muscle_list = self.DB_EXERCISES.get_exercises_by_muscle_list(
            choice
        )
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
        (
            exercise_type,
            equipment,
            difficulty,
            instructions,
        ) = self.DB_EXERCISES.get_exercise_entry(choice)[0]
        # Exercise type
        AuthenticityMainWindow._change_disabled_input_value(
            self.infobox_frame.label_type_entry, 0, exercise_type
        )
        # Exercise equipment
        AuthenticityMainWindow._change_disabled_input_value(
            self.infobox_frame.label_equip_entry, 0, equipment
        )
        # Exercise difficulty
        AuthenticityMainWindow._change_disabled_input_value(
            self.infobox_frame.label_difficulty_entry, 0, difficulty
        )
        # Exercise instructions
        AuthenticityMainWindow._change_disabled_input_value(
            self.infobox_frame.textbox_infobox, 1.0, instructions
        )


class _ExerciseInfoBox(customtkinter.CTkFrame):
    INPUT_WIDGET_WIDTH = 280

    def __init__(self, master) -> None:
        super().__init__(master, width=self.INPUT_WIDGET_WIDTH)
        # Type Label
        self.label_type = customtkinter.CTkLabel(self, text="Type")
        self.label_type.grid(row=0, column=0, padx=10, pady=(10, 0))
        # Type Entry
        self.label_type_entry = customtkinter.CTkEntry(
            self, width=self.INPUT_WIDGET_WIDTH, state="disabled"
        )
        self.label_type_entry.grid(row=1, column=0, padx=10, pady=0)
        # Equipment Label
        self.label_equip = customtkinter.CTkLabel(self, text="Equipment")
        self.label_equip.grid(row=4, column=0)
        # Equipment Entry
        self.label_equip_entry = customtkinter.CTkEntry(
            self, width=self.INPUT_WIDGET_WIDTH, state="disabled"
        )
        self.label_equip_entry.grid(row=5, column=0)
        # Difficulty Label
        self.label_difficulty = customtkinter.CTkLabel(self, text="Difficulty")
        self.label_difficulty.grid(row=6, column=0)
        # Difficulty Entry
        self.label_difficulty_entry = customtkinter.CTkEntry(
            self, width=self.INPUT_WIDGET_WIDTH, state="disabled"
        )
        self.label_difficulty_entry.grid(row=7, column=0)
        # Infobox Label
        self.label_infobox = customtkinter.CTkLabel(self, text="Instruction")
        self.label_infobox.grid(row=8, column=0)
        # Infobox Textbox
        self.textbox_infobox = customtkinter.CTkTextbox(
            self,
            width=self.INPUT_WIDGET_WIDTH,
            state="disabled",
            wrap="word",
        )
        self.textbox_infobox.grid(row=9, column=0, padx=15, pady=(0, 15), sticky="nsew")


class _WorkoutCalender(customtkinter.CTkTabview):

    def __init__(self, master):
        super().__init__(master)

        self.add("Sunday")
        self.add("Monday")
        self.add("Tuesday")
        self.add("Wednesday")
        self.add("Thursday")
        self.add("Friday")
        self.add("Saturday")

        # Sunday
        self.sun_tab = customtkinter.CTkLabel(master=self.tab("Sunday"), text="Sunday")
        self.sun_tab.grid(row=0, column=0, padx=10, pady=10)

        # Monday
        self.mon_tab = customtkinter.CTkLabel(master=self.tab("Monday"), text="Monday")
        self.mon_tab.grid(row=0, column=0, padx=10, pady=10)

        # Tuesday
        self.tue_tab = _WorkoutTab(self.tab("Tuesday"), "Tuesday")
        self.tue_tab.grid(row=0, column=0, padx=10, pady=10)


class _WorkoutTab(customtkinter.CTkFrame):
    INPUT_WIDGET_WIDTH = 400

    def __init__(self, master, text):
        super().__init__(master, width=self.INPUT_WIDGET_WIDTH)

        self.tab_label = customtkinter.CTkLabel(self, text=text)
        self.tab_label.grid(row=0, column=0, padx=0, pady=0)

