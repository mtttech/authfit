import datetime
from tkinter import *

import customtkinter

from authfit.assets import get_exercises_by_group, get_muscle_groups


class ExerciseSelectionWidget(customtkinter.CTkFrame):
    W_ENTRY_WIDTH = 30

    def __init__(self, master) -> None:
        super().__init__(master)
        self.entry_secs_state = True
        self.entry_wgt_state = True

        ex_reps = customtkinter.CTkLabel(self, text="Set")
        ex_wgt = customtkinter.CTkLabel(self, text="Weight")
        ex_secs = customtkinter.CTkLabel(self, text="Seconds")

        self.ex_selector = customtkinter.CTkOptionMenu(
            self,
            anchor="center",
            state="disabled",
            values=["[ SELECT A MUSCLE GROUP FIRST ]"],
            width=300,
        )
        self.ex_reps1 = customtkinter.CTkEntry(
            self,
            width=self.W_ENTRY_WIDTH,
        )
        self.ex_reps2 = customtkinter.CTkEntry(
            self,
            width=self.W_ENTRY_WIDTH,
        )
        self.ex_reps3 = customtkinter.CTkEntry(
            self,
            width=self.W_ENTRY_WIDTH,
        )
        self.ex_wgt1 = customtkinter.CTkEntry(
            self,
            width=self.W_ENTRY_WIDTH,
        )
        self.ex_wgt2 = customtkinter.CTkEntry(
            self,
            width=self.W_ENTRY_WIDTH,
        )
        self.ex_wgt3 = customtkinter.CTkEntry(
            self,
            width=self.W_ENTRY_WIDTH,
        )
        self.ex_secs1 = customtkinter.CTkEntry(
            self,
            width=self.W_ENTRY_WIDTH,
        )
        self.ex_secs2 = customtkinter.CTkEntry(
            self,
            width=self.W_ENTRY_WIDTH,
        )
        self.ex_secs3 = customtkinter.CTkEntry(
            self,
            width=self.W_ENTRY_WIDTH,
        )
        self.ex_wgt_na = customtkinter.CTkButton(
            self,
            command=self.toggle_wgt_state,
            text="Weight N/A",
            width=60,
        )
        self.ex_secs_na = customtkinter.CTkButton(
            self,
            command=self.toggle_secs_state,
            text="Seconds N/A",
            width=60,
        )

        ex_reps.grid(row=0, column=1, columnspan=3, padx=2, pady=2)
        ex_wgt.grid(row=0, column=4, columnspan=3, padx=2, pady=2)
        ex_secs.grid(row=0, column=7, columnspan=3, padx=2, pady=2)

        self.ex_selector.grid(row=1, column=0, padx=2, pady=2)
        self.ex_reps1.grid(row=1, column=1, padx=5, pady=2)
        self.ex_reps2.grid(row=1, column=2, padx=2, pady=2)
        self.ex_reps3.grid(row=1, column=3, padx=2, pady=2)
        self.ex_wgt1.grid(row=1, column=4, padx=2, pady=2)
        self.ex_wgt2.grid(row=1, column=5, padx=2, pady=2)
        self.ex_wgt3.grid(row=1, column=6, padx=2, pady=2)
        self.ex_secs1.grid(row=1, column=7, padx=2, pady=2)
        self.ex_secs2.grid(row=1, column=8, padx=2, pady=2)
        self.ex_secs3.grid(row=1, column=9, padx=2, pady=2)
        self.ex_wgt_na.grid(row=1, column=10, padx=2, pady=2)
        self.ex_secs_na.grid(row=1, column=11, padx=2, pady=2)

    def toggle_secs_state(self) -> None:
        self.ex_secs1.delete(0, END)
        self.ex_secs2.delete(0, END)
        self.ex_secs3.delete(0, END)

        if self.entry_secs_state:
            self.entry_secs_state = False
            self.ex_secs1.configure(state="disabled")
            self.ex_secs2.configure(state="disabled")
            self.ex_secs3.configure(state="disabled")
        else:
            self.entry_secs_state = True
            self.ex_secs1.configure(state="normal")
            self.ex_secs2.configure(state="normal")
            self.ex_secs3.configure(state="normal")

    def toggle_wgt_state(self) -> None:
        self.ex_wgt1.delete(0, END)
        self.ex_wgt2.delete(0, END)
        self.ex_wgt3.delete(0, END)

        if self.entry_wgt_state:
            self.entry_wgt_state = False
            self.ex_wgt1.configure(state="disabled")
            self.ex_wgt2.configure(state="disabled")
            self.ex_wgt3.configure(state="disabled")
        else:
            self.entry_wgt_state = True
            self.ex_wgt1.configure(state="normal")
            self.ex_wgt2.configure(state="normal")
            self.ex_wgt3.configure(state="normal")


class ApplicationWindow(customtkinter.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)

        self.wo_name = customtkinter.CTkEntry(
            self,
            placeholder_text="Workout Name",
            width=400,
        )
        self.wo_date = customtkinter.CTkEntry(
            self,
            placeholder_text=str(datetime.date.today()),
            width=400,
        )
        self.wo_date.configure(state="disabled")
        self.wo_group = customtkinter.CTkOptionMenu(
            self,
            values=[m[0] for m in get_muscle_groups()],
            width=400,
            command=self.activate_selector,
            anchor="center",
        )
        self.wr1 = ExerciseSelectionWidget(self)
        self.wr2 = ExerciseSelectionWidget(self)
        self.wr3 = ExerciseSelectionWidget(self)
        self.wr4 = ExerciseSelectionWidget(self)
        self.notes = customtkinter.CTkTextbox(self, height=80, wrap="word")
        self.save_btn = customtkinter.CTkButton(self, text="Save Workout")

        self.wo_name.grid(row=0, column=0, padx=5, pady=(10, 5), sticky="w")
        self.wo_date.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.wo_group.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.wr1.grid(row=3, column=0)
        self.wr2.grid(row=4, column=0)
        self.wr3.grid(row=5, column=0)
        self.wr4.grid(row=6, column=0)
        self.notes.grid(row=7, column=0, padx=5, pady=5, sticky="we")
        self.save_btn.grid(row=8, column=0, pady=(5, 10))
 
    def activate_selector(self, choice) -> None:
        exercises_by_group = [e[0] for e in get_exercises_by_group(choice)]
        self.wr1.ex_selector.configure(state="normal", values=exercises_by_group)
        self.wr1.ex_selector.set(exercises_by_group[0])
        self.wr2.ex_selector.configure(state="normal", values=exercises_by_group)
        self.wr2.ex_selector.set(exercises_by_group[0])
        self.wr3.ex_selector.configure(state="normal", values=exercises_by_group)
        self.wr3.ex_selector.set(exercises_by_group[0])
        self.wr4.ex_selector.configure(state="normal", values=exercises_by_group)
        self.wr4.ex_selector.set(exercises_by_group[0])


class Application(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.title("AuthFit")

        self.textbox = ApplicationWindow(self)
        self.textbox.grid(row=0, column=0)
