from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Button

from screen.app_screens import HomeScreen, ChooseScreen
from screen.modal_screens import RequestQuitScreen

class SudokuApp(App):
    BINDINGS = [
        Binding("s", "screen_notification", "Show Screen Stack", show=False),
        ("q", "request_quit", "Quit"),
        ("h", "go_to_home", "Home")
    ]

    #CSS_PATH = "demo.tcss"

    SCREENS = {
        "home": HomeScreen,
        "request_quit": RequestQuitScreen,
        "choose": ChooseScreen
    }

    def check_action(self, action: str, parameters: tuple[object, ...]) -> bool | None:

        if action == "go_to_home" and str(self.screen) == "HomeScreen()":
            return None
        return True

    def action_request_quit(self) -> None:

        def check_quit(quit: bool | None) -> None:
            if quit:
                self.exit()

        self.push_screen("request_quit", check_quit)


    def action_go_to_home(self) -> None:
        self.pop_screen()

    def on_mount(self) -> None:
        self.push_screen("home")
        self._screen_stack.pop(0)

    def action_screen_notification(self) -> None:
        #self.notify(str(self.screen_stack))
        #self.notify(str(self.screen.size))
        self.notify(str())


if __name__ == "__main__":
    app = SudokuApp()
    app.run()