
from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from random import random

class FBLAQuiz(App):
    def __init__(self, **kwargs) -> None:
            self.option_one = "option a"
            self.option_two = "option b"
            self.option_three = "option c"
            self.option_four = "option d"

            super(FBLAQuiz, self).__init__(**kwargs)

            self.cols = 4
            self.rows = 4

            # self.row_default_height = 75
            # self.row_force_default = True
    

class FBLAQuizApp(App):
    def build(self):
        # return FBLAQuiz()            
        pass


if __name__ == "__main__":
    FBLAQuizApp().run()
