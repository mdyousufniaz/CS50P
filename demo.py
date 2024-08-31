from textual.app import App, ComposeResult
from textual.widgets import Digits, Static
from textual.widget import Widget
from textual.reactive import var
from textual.geometry import Offset


class SimpleCounter(Static):

    DEFAULT_CSS = """
       SimpleCounter {
            background: $boost-darken-3;
            width: 15;
            align: center middle;
            border: hkey $warning;
            border-title-align: center;
            border-title-style: bold italic;
        
            Digits {
                background: $surface;
                width: auto;
                text-style: bold;
                color: floralwhite;
            }
        }
    """

    BORDER_TITLE = "MOVES"

    value = 0

    def compose(self) -> ComposeResult:
        self.counter_display = Digits(str(self.value))
        yield self.counter_display

    def increment(self) -> None:
        self.value += 1
        self.counter_display.update(str(self.value))


class MyApp(App):
    def compose(self) -> ComposeResult:
        self.widget = SimpleCounter()
        yield self.widget

    def on_key(self, event):
        if event.key == "i":
            self.widget.increment()

MyApp().run()