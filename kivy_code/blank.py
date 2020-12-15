from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class BlankScreen(Screen):
    text = StringProperty("Fill in the Blank question")
    response = ""

    answer = ""

    def select(self, param):
        self.response = param.strip().lower()
    
    def set_questions(self, qs: list):
        self.questions = qs
    
    def on_pre_enter(self):
        for q in self.questions:
            if q.type == "blank":
                self.text = q.text
                self.answer = q.answer