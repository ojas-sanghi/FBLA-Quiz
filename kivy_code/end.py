from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, ListProperty

import kivymd_extensions.akivymd

class EndScreen(Screen):
    questions_correct = ListProperty([False, False, False, False, False])
    total_correct = NumericProperty(0)

    def set_response_data(self, qs_correct: list):
        self.questions_correct = qs_correct

        self.total_correct = self.questions_correct.count(True)

    def on_pre_enter(self):
        two_d_labels = []
        # get all the boxes underneath the "MDBoxLayout" whose id is "box_of_labels_box"
        # add the labels which are children of those boxes to a list
        for box in self.ids.box_of_labels_box.children:
            two_d_labels.append(box.children)
        two_d_labels.reverse()

        question_num = 1        
        for label_list in two_d_labels:
            for label in label_list:
                # CorrectResultLabel
                if label.text == "Incorrect":
                    if self.questions_correct[question_num - 1]:
                        label.text = "Correct"
                        label.text_color = [0, 0.4, 0, 1]
                    else:
                        label.text = "Incorrect"
                        label.text_color = [1, 0, 0, 1]
                # QuestionResultLabel
                else:
                    label.text = f"Question {question_num}: "
            
            question_num += 1

    def on_enter(self, *args):
        progress_circle = self.ids.progress
        progress_circle.current_percent = self.total_correct