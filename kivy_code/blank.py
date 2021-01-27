from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty


class BlankScreen(Screen):
    question = None
    text = StringProperty("Fill in the Blank question")

    def select(self, param):
        self.question.response = param.strip().lower()

    def set_questions(self, qs: list):
        self.questions = qs

    def on_pre_enter(self):
        self.reset()
        for q in self.questions:
            if q.type == "blank":
                self.question = q
                self.text = q.text

    def reset(self):
        self.ids.text_field.text = ""