from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty


class CheckboxScreen(Screen):
    question = None
    text = StringProperty("Checkbox Question")
    options = ListProperty(["option 1", "option 2", "option 3", "option 4"])

    def select(self, param):
        # unselect if already selected
        if self.options[param] in self.question.response:
            self.question.response.remove(self.options[param])
        else:
            self.question.response.append(self.options[param])
        self.question.response = sorted(self.question.response)

    def set_questions(self, qs: list):
        self.questions = qs

    def on_pre_enter(self):
        self.reset()
        for q in self.questions:
            if q.type == "checkbox":
                self.question = q
                self.text = q.text
                self.options = q.options

    def reset(self):
        self.ids.check1.active = False
        self.ids.check2.active = False
        self.ids.check3.active = False
        self.ids.check4.active = False