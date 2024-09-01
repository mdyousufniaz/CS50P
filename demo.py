from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Grid

class Cell(Static):

    DEFAULT_CSS = """
        Cell {
            height: 3;
            width: 3;
            padding: 1;
            color: $text;
        }
    """

class SudokuGrid3X3(Grid):

    DEFAULT_CSS = """
        SudokuGrid3X3 {
            grid-columns: 9;
            
            background: $background;
            grid-gutter: 1;
            border: solid blue;
        }
    """

    def compose(self) -> ComposeResult:
        self.cells = [Cell(str(index)) for index in range(1, 82)]
        yield from self.cells

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield SudokuGrid3X3()


MyApp().run()