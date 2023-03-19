import customtkinter


class ExerciseInfoBox(customtkinter.CTkFrame):
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
            self, width=self.INPUT_WIDGET_WIDTH, state="disabled", wrap="word",
        )
        self.textbox_infobox.grid(row=9, column=0, padx=15, pady=(0, 15), sticky="nsew")
