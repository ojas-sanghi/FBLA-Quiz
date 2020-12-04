from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class MCQScreen(Screen):
    question = StringProperty("MCQ Question")

    option_1 = StringProperty("option 1")
    option_2 = StringProperty("option 2")
    option_3 = StringProperty("option 3")
    option_4 = StringProperty("option 4")

    answer_index = 0

    def select(self, param):
        self.answer_index = param

    
    def set_questions(self, qs: list):
        self.questions = qs
    
    def on_pre_enter(self):
        for q in self.questions:
            if q.type == "mcq":
                self.question = q.text
                self.option_1 = q.options[0]
                self.option_2 = q.options[1]
                self.option_3 = q.options[2]
                self.option_4 = q.options[3]
