from textual.app import App
from textual.widget import Widget

class MyWidget(Widget):
    def on_key(self):
        self.app.notify('Hello')

class MyApp(App):
    def compose(self):
        self.my_widget = MyWidget()
        yield self.my_widget

    def on_key(self):
        self.my_widget.on_key()


MyApp().run()