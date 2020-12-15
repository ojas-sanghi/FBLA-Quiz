from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class TFScreen(Screen):
    text = StringProperty("T/F question")
    response = ""

    answer = ""

    def select(self, param):
        self.response = param

    def set_questions(self, qs: list):
        self.questions = qs
    
    def on_pre_enter(self):
        for q in self.questions:
            if q.type == "tf":
                self.text = q.text
                self.answer = q.answer