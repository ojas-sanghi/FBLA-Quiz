from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty


class TFScreen(Screen):
    question = None
    text = StringProperty("T/F question")

    def select(self, param):
        # unselect if already selected
        if self.question.response == param:
            self.question.response = None
        else:
            self.question.response = param

    def set_questions(self, qs: list):
        self.questions = qs

    def on_pre_enter(self):
        self.reset()
        for q in self.questions:
            if q.type == "tf":
                self.question = q
                self.text = q.text

    def reset(self):
        self.ids.radio1.active = False
        self.ids.radio2.active = False
