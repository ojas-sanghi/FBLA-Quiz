from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty


class MCQScreen(Screen):
    question = None
    text = StringProperty("MCQ Question")
    options = ListProperty(["option 1", "option 2", "option 3", "option 4"])

    def select(self, param):
        # unselect if already selected
        if self.question.response == self.options[param]:
            self.question.response = None
        else:
            self.question.response = self.options[param]

    def set_questions(self, qs: list):
        self.questions = qs

    def on_pre_enter(self):
        self.reset()
        for q in self.questions:
            if q.type == "mcq":
                self.question = q
                self.text = q.text
                self.options = q.options

    def reset(self):
        self.ids.radio1.active = False
        self.ids.radio2.active = False
        self.ids.radio3.active = False
        self.ids.radio4.active = False