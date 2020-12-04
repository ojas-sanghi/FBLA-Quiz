from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class TFScreen(Screen):
    question = StringProperty("T/F question")

    def select(self, param):
        self.answer = param

    def set_questions(self, qs: list):
        self.questions = qs
    
    def on_pre_enter(self):
        for q in self.questions:
            if q.type == "tf":
                self.question = q.text