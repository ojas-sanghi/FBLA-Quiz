from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty


class SAQScreen(Screen):
    question = None
    text = StringProperty("Short Answer Question")

    def select(self, param):
        self.question.response = param.strip().lower()

    def set_questions(self, qs: list):
        self.questions = qs

    def on_pre_enter(self):
        self.reset()
        q_num = 0
        for q in self.questions:
            if q.type == "saq":
                q_num = self.questions.index(q) + 1

                self.question = q
                self.text = q.text + f" (Question {q_num}/5)"

    def reset(self):
        self.ids.text_field.text = ""
