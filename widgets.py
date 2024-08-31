from textual.widgets import Digits, Static
from textual.reactive import var
from textual.timer import Timer
from textual.app import ComposeResult

from typing import Optional

from time import monotonic

class CustomTimer(Digits):

    DEFAULT_CSS = """
        CustomTimer {
            background: $boost-darken-3;
            width: auto;
            padding: 1;
            border: hkey $warning;
            border-title-align: center;
            border-title-style: bold italic;
            text-style: bold;
            color: floralwhite;
        }
    """
  
    BORDER_TITLE = "TIMER"

    start_time: Optional[float] = None
    total_time: float = 0.0
    pause: var[bool] = var(True, init=False)

    def spended_time(self) -> float:
        if self.start_time is None:
            return 0.0
        return self.total_time + monotonic() - self.start_time
    
    def update_display(self) -> None:
        minutes, seconds = divmod(self.spended_time(), 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")


    def on_mount(self) -> None:
        self.update_display()
        self.timer: Timer = self.set_interval(1, self.update_display, pause=self.pause)

    def watch_pause(self) -> None:
        #self.app.notify("Inside Watch")
        if self.pause:
            self.timer.pause()
        else:
            self.timer.resume()
        

    def start_timer(self) -> None:
        if self.pause:
            self.start_time = monotonic()
            self.pause = False
        else:
            self.app.notify("Timer is already Running!")

    def stop_timer(self) -> None:
        if self.pause:
            self.app.notify("Timer is already Stopped!")
        else:
            self.pause = True
            self.total_time = self.spended_time()
            
    def reset_timer(self) -> None:
        self.pause = True
        self.start_time = None
        self.total_time = 0.0
        self.update_display()

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