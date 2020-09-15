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


def pressed(input):
    value = self.input
    value = ""


def run_cal(input):
    input_Ver = eval_input(input)
    print(input_Ver)
    Calculator1 = input_to_obj(input_Ver)
    result = calculate(Calculator1)

    return result


class YourApp(App):

    def build(self):
        root_widget = BoxLayout(
            orientation='vertical')

        # root_widget = FloatLayout(
        #    size=(200, 200))

        red = [1, 0, 0, 1]
        green = [0, 1, 0, 1]
        blue = [0, 0, 1, 1]
        purple = [1, 0, 1, 1]
        orange = [255, 165, 0, 1]

        title = Label(text="Compound Interest Calculator",
                      font_size=40, size_hint=(0.7, 1))
        description = Label(text="TEMP")

        inputlabel1 = Label(text="TEMP")
        inputlabel2 = Label(text="TEMP")
        inputlabel3 = Label(text="TEMP")
        inputlabel4 = Label(text="TEMP")

        input1 = TextInput(multiline=False)
        input2 = TextInput(multiline=False)
        input3 = TextInput(multiline=False)
        input4 = TextInput(multiline=False)

        calculate_button = Button(text="Calculate", background_color=orange)
        clear_button = Button(text="Clear")

       # calculate_button.bind(on_press=lambda x: printtest())
        calculate_button.bind(on_press=lambda x: run_cal(
            (input1.text, input2.text, input3.text, input4.text)))

        clear_button.bind(on_press=pressed(self.input1))

       # calculate_button.bind(on_press=run_cal((input1, input2, input3, input4)))

        input_grid = GridLayout(cols=2, size_hint_y=2)

        input_grid.add_widget(inputlabel1)
        input_grid.add_widget(input1)
        input_grid.add_widget(inputlabel2)
        input_grid.add_widget(input2)
        input_grid.add_widget(inputlabel3)
        input_grid.add_widget(input3)
        input_grid.add_widget(inputlabel4)
        input_grid.add_widget(input4)

        root_widget.add_widget(title)
        root_widget.add_widget(description)
        root_widget.add_widget(input_grid)
        root_widget.add_widget(calculate_button)
        root_widget.add_widget(clear_button)
        return root_widget


YourApp().run()
