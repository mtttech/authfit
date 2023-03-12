from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class AuthenticityApp(App):
    def __init__(self):
        print("Authenticity App main.")


def main():
    AuthenticityApp()


if __name__ == "__main__":
    main()
