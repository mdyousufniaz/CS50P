from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Label, Button
#from textual import on

from art import text2art


class BaseModel(ModalScreen[bool]):

    DEFAULT_CSS = """
        BaseModel {
            align: center middle;

            Vertical {
                background: $panel-darken-2;
                width: 50%;
                height: 50%;
                border: vkey $primary;

                Label {
                    text-style: bold;
                }

                .app-name {
                    color: $warning-lighten-3;
                }

            }

        }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label(text2art("PySudoku", font="tarty2"), classes="app-name")
            yield Label(id='title')

class RequestQuitScreen(BaseModel):

    DEFAULT_CSS = """
        RequestQuitScreen {
            Vertical {
                #title {
                    height: 40%;
                    width: 100%;
                    content-align: center middle;
                }

                Horizontal {
                    align: center middle;
                    Button {
                        width: 1fr;
                        margin: 3;
                    }
                }
            }

        }
    """

    def on_mount(self) -> None:
        self.query_one('#title', Label).update("Do You Want to Quit PySudoku ?")

        self.query_one(Vertical).mount(
            Horizontal(
                Button("Yes", variant="error", id="yes"),
                Button("No", variant="primary", id="no")
            )
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "yes")
        