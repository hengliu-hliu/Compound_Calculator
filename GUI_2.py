from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from Compound_Interest import *
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window


#Author: Henry
# Program to calculate compounded growth


class PopupIcon(Popup):
    inputs = StringProperty()
    results = StringProperty()

    def dismiss_popup(self):
        self.dismiss()


class MyGrid(Widget):
    test3 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        Window.bind(on_key_down=self._on_keyboard_down)

    principal = ObjectProperty(None)
    interest_rate = ObjectProperty(None)
    compound_rate = ObjectProperty(None)
    years = ObjectProperty(None)

    def btn_calculate(self):

        output = run_cal((self.principal.text, self.interest_rate.text,
                          self.compound_rate.text, self.years.text))

        popup = PopupIcon(title='Result:')

        popup.results = str(output)

        #print(self.test3)
        popup.open()

    def btn_clear(self):
        self.principal.text = ""
        self.interest_rate.text = ""
        self.compound_rate.text = ""
        self.years.text = ""

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):

        #print(self.test3)

        if self.test3 and keycode == 40:  # 40 - Enter key pressed
            self.btn_calculate()
            self.focus_change()

    def focus_change(self):

        if self.test3:
            self.test3 = False
        else:
            self.test3 = True


class MyApp(App):

    def build(self):
        return MyGrid()


MyApp().run()
