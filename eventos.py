
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


class Eventos:
    def on_dismiss(self, arg):
        try:
            inputtext =TextInput(text="Ingrese o evento")
            self.popup=inputtext
            self.popup.bind(on_dismiss=self.on_dismiss)
        except Exception as error:
            print(error)