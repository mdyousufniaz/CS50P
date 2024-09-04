from textual.app import App, ComposeResult
from textual.widgets import Digits
from textual.containers import Vertical, Middle
from textual.geometry import Offset
from textual import work

from random import randint
from textual.reactive import reactive

class AnimatedDigits(Middle):
    DEFAULT_CSS = """
        AnimatedDigits {
            height: auto;
            width: auto;
        }
        
    """

    def __init__(self, display: str):
        self.animated_digits = [
            AnimatedDigit(digit)
            for digit in display
        ]
    
    def compose(self):
        yield from self.animated_digits

    def update(self, new_display):
        for animated_digit in self.animated_digits:
            animated_digit.up

    a = reactive(True)

class AnimatedDigit(Vertical):

    DEFAULT_CSS = """
        AnimatedDigit {
            height: 3;
            width: 3;

            Vertical {
                height: 6;
            }
        }

    """

    def __init__(self, value: str) -> None:
        super().__init__()
        self.value = value

    def compose(self) -> ComposeResult:
        self.inner_vertical = Vertical()
        with self.inner_vertical:
            yield Digits(self.value)

    def update(self, new_value: str) -> None:
        self.inner_vertical.mount(Digits(new_value))

        self.inner_vertical.animate(
            "offset",
            value=Offset(0, -4),
            final_value=Offset(0, 0),
            on_complete=self.query(Digits).first().remove,
            duration=0.9
        )

    def on_mount(self):
        self.set_interval(0.7, self.add_digit, repeat=5)


    def add_digit(self):
        self.update(str(randint(1, 9)))

class MyApp(App):
    def compose(self):
        self.my_digit = AnimatedDigit("0")
        yield self.my_digit
    
    def key_up(self):
        self.my_digit.add_digit()



MyApp().run()