from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Grid
from textual.message import Message
from textual import events
from textual.reactive import var
from textual import on

class Cell(Static):

    selected = var(False)

    DEFAULT_CSS = """
        Cell {
            height: 1;
            width: 3;
            color: $text;
            text-align: center;
            background: $background;
        }

        Cell.-selected {
            background: blue; /* or any color for the selected cell */
        }
    """

    def on_click(self, event: events.Click) -> None:
        # Emit a custom event to notify the grid that this cell was clicked
        
        self.post_message(self.Clicked(self))

    class Clicked(Message):
        def __init__(self, cell):
            self.cell = cell
            super().__init__()

    def watch_selected(self, selected: bool) -> None:
        if selected:
            self.add_class("-selected")
        else:
            self.remove_class("-selected")

class SudokuGrid3X3(Grid):

    DEFAULT_CSS = """
        SudokuGrid3X3 {
            box-sizing: content-box;
            grid-size: 9;
            width: 40;
            height: 23;
            padding-top: 2;
            padding-left: 1;
            keyline: thin $secondary;
            background: $background;
            grid-gutter: 0 1;
        }

        SudokuGrid3X3:focus {
            border: solid blue;
        }

    """

    def compose(self) -> ComposeResult:
        self.cells = [
            [Cell(str((row * 9 + col) % 10)) for col in range(9)]
            for row in range(9)
        ]
        for row in self.cells:
            yield from row

    def can_focus(self) -> bool:
        # Make the grid focusable
        return True

    def on_blur(self, event: events.Blur) -> None:
        if self.selected_cell:
            self.selected_cell.selected = False
            self.selected_cell = None

    def on_mount(self) -> None:
        # To track the currently selected cell
        self.selected_cell = None
        self.selected_row = 0
        self.selected_col = 0

    def on_cell_clicked(self, event: Cell.Clicked) -> None:
        self.app.notify('Hello')
        clicked_cell = event.cell

        # Reset the previous selected cell's background if any
        if self.selected_cell and self.selected_cell != clicked_cell:
            self.selected_cell.selected = False

        # Set the new selected cell's background
        clicked_cell.selected = True
        self.selected_cell = clicked_cell

        for r in range(9):
            for c in range(9):
                if self.cells[r][c] == clicked_cell:
                    self.selected_row = r
                    self.selected_col = c
                    break
            
        self.focus()

        @on(events.Key)                
        def on_key(self, event: events.Key) -> None:
        # Handle arrow key navigation
            if event.key == "up" and self.selected_row > 0:
                self.move_selection(self.selected_row - 1, self.selected_col)
            elif event.key == "down" and self.selected_row < 8:
                self.move_selection(self.selected_row + 1, self.selected_col)
            elif event.key == "left" and self.selected_col > 0:
                self.move_selection(self.selected_row, self.selected_col - 1)
            elif event.key == "right" and self.selected_col < 8:
                self.move_selection(self.selected_row, self.selected_col + 1)

    def move_selection(self, new_row: int, new_col: int) -> None:
        # Deselect the current cell
        if self.selected_cell:
            self.selected_cell.selected = False

        # Update the selected cell coordinates
        self.selected_row, self.selected_col = new_row, new_col
        self.selected_cell = self.cells[new_row][new_col]
        self.selected_cell.selected = True

    

class MyApp(App):

    CSS = """
    Input .input--cursor {
        color: blue;
    }
    """

    def compose(self) -> ComposeResult:
        yield SudokuGrid3X3()

    # def key_up(self):
    #     self.notify(str(self.screen.size))


MyApp().run()