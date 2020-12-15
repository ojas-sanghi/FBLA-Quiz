from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty

class CheckboxScreen(Screen):
    text = StringProperty("Checkbox Question")
    options = ListProperty(["option 1", "option 2", "option 3", "option 4"])
    response = []

    answer = []

    def select(self, param):
        # unselect if already selected
        if self.options[param] in self.response:
            self.response.remove(self.options[param])
        else:
            self.response.append(self.options[param])
        
    def set_questions(self, qs: list):
        self.questions = qs
    
    def on_pre_enter(self):
        for q in self.questions:
            if q.type == "checkbox":
                self.text = q.text
                self.options = q.options
                self.answer = q.answer