from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class BlankScreen(Screen):
    question = StringProperty("Fill in the Blank question")

    def select(self, param):
        self.answer = param
    
    def set_questions(self, qs: list):
        self.questions = qs
    
    def on_pre_enter(self):
        for q in self.questions:
            if q.type == "blank":
                self.question = q.text