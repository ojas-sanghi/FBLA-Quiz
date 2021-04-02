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
        q_num = 0
        for q in self.questions:
            if q.type == "tf":
                q_num = self.questions.index(q) + 1

                self.question = q
                self.text = q.text + f" (Question {q_num}/5)"

    def reset(self):
        self.ids.radio1.active = False
        self.ids.radio2.active = False
