from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class SAQScreen(Screen):
    text = StringProperty("Short Answer Question")
    response = ""

    answer = ""

    def select(self, param):
        self.response = param.strip().lower()

    def set_questions(self, qs: list):
        self.questions = qs
    
    def on_pre_enter(self):
        for q in self.questions:
            if q.type == "saq":
                self.text = q.text
                self.answer = q.answer