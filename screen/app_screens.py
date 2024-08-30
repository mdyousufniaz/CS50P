from textual.screen import Screen
from textual.widgets import Label, Footer, Button, Select
from textual.app import ComposeResult
from textual.containers import Container, Vertical, Horizontal, Grid
from textual import on

from art import text2art

class BaseScreen(Screen):

    DEFAULT_CSS = """
        BaseScreen {
            border: vkey $success;
            align-horizontal: center;

            Container {
                background: $background;
                align-vertical: middle;
                height: 23%;
                padding-bottom: 1;

                Label {
                    color: $warning-lighten-3;
                    text-style: bold;
                    margin-bottom: 2;
                }
            }

            Vertical {
                align: center middle;

                Button {
                    margin: 2;
                }
            }
    }
    """

    def __init__(self, tarty_font_num: int) -> None:
        self.tarty_font_num = tarty_font_num
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Container(Label(text2art("PySudoku", font="tarty" + str(self.tarty_font_num))))
        yield Vertical()
        yield Footer()

class BaseScreen1(BaseScreen):

    DEFAULT_CSS = """
        BaseScreen1 {
            Container {
                align-horizontal: center;
                height: 23%;
            }
        }
    """

    def __init__(self) -> None:
        super().__init__(tarty_font_num=1)


class BaseScreen2(BaseScreen):

    DEFAULT_CSS = """
        BaseScreen1 {
            Container {
                align-horizontal: left;
                height: 15%;
            }
        }
    """

    def __init__(self) -> None:
        super().__init__(tarty_font_num=2)
        


class HomeScreen(BaseScreen1):

    def on_mount(self) -> None:
        self.query_one(Vertical).mount(
            Button("New Game", variant="primary", id="new-game"),
            Button("Leader Board", variant="primary"),
            Button("Quit", variant="primary", id="quit")
        )

    @on(Button.Pressed, "#new-game")
    def push_choose_screen(self) -> None:
        self.app.push_screen("choose")

    @on(Button.Pressed, "#quit")
    def request_quit_screen(self) -> None:
        self.app.action_request_quit()
    
class ChooseScreen(BaseScreen1):


    def on_mount(self) -> None:
        SELECT_TEXT = "Choose a difficulity"

        self.query_one(Vertical).mount(
            Select.from_values(
                ("Easy", "Medium", "Hard"),
                prompt= SELECT_TEXT
            ),
            Button("Start Game", variant="success"),
            Button("Back to Home", variant="error", id="back")
        )

        self.query_one(Select).styles.width = len(SELECT_TEXT) + 10
    
    @on(Button.Pressed, "#back")
    def handle_back_to_home(self) -> None:
        self.app.action_go_to_home()

    

