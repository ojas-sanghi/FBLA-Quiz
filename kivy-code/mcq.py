from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class MCQScreen(Screen):
    question = StringProperty("this is a multiple choice question")

    option_1 = "option 1"
    option_2 = "option 2"
    option_3 = "option 3"
    option_4 = "option 4"

    def select(self, param):
        print(param)
        self.question = "cool MCQ question"

        print(self.ids)