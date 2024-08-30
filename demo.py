from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Digits
from textual.widget import Widget
from textual.reactive import var


class MyDigit(Widget):

    DEFAULT_CSS = """
        MyDigit {
        
            Vertical {
                width: 3;
            }

            #first {
                height: 3;
                background: lime;
            }

            #second {
                height: auto;
                background: skyblue;
            }
        }
    """

    current_value = var(0, init=False)

    def compose(self) -> ComposeResult:
        with Vertical():
            self.v_box = Vertical()
            with self.v_box:
                yield Digits(str(self.current_value))
    
    def add_one(self):
        self.current_value += 1

    def watch_current_value(self, new):
        self.v_box.mount(Digits(str(new)))
        prev_offset = self.v_box.styles.offset
        new_offset = -3
        self.v_box.styles.animate("offset", value=new_offset, duration=0.5, on_complete=self.remove_prev_digit)
        self.v_box.styles.offset = (0, 0)

    def remove_prev_digit(self):
        self.v_box.query(Digits).first().remove()


class MyApp(App):
    def compose(self) -> ComposeResult:
        self.widget = MyDigit()
        yield self.widget

    def on_key(self, event):
        if event.key == "u":
            self.widget.add_one()

MyApp().run()