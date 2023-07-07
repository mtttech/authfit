import customtkinter

from authfit.gui import Application


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def main() -> None:
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()
