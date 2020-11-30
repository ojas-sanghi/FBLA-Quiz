
from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivymd.app import MDApp

from random import random

class FBLAQuiz(MDApp):
    def __init__(self, **kwargs) -> None:
            super(FBLAQuiz, self).__init__(**kwargs)

    
    def select(self, param):
        print(param)
    
    def build(self):
        self.theme_cls.theme_style = "Light"

if __name__ == "__main__":
    FBLAQuiz().run()
