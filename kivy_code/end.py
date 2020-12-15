from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, ListProperty
import kivy.factory 

class EndScreen(Screen):
    questions_correct = ListProperty([False, False, False, False, False])
    total_correct = NumericProperty(0)

    def set_response_data(self, qs_correct: list):
        self.questions_correct = qs_correct

        self.total_correct = self.questions_correct.count(True)

        print(self.questions_correct)
    
    def on_pre_enter(self, *args):

        # set "total correct" label to correct number
        total_label = self.ids.results
        total_label.text = f"Total Correct: {self.total_correct}/5"


        twod_labels = []
        # get all the boxes underneath the "MDBoxLayout" whose id is "box_of_labels_box"
        # add the labels which are children of those boxes to a list
        for box in self.ids.box_of_labels_box.children:
            twod_labels.append(box.children)
        twod_labels.reverse()

        question_num = 1        
        for label_list in twod_labels:
            for label in label_list:
                # CorrectResultLabel
                if label.text == "Incorrect":
                    if self.questions_correct[question_num - 1]:
                        label.text = "Correct"
                        label.text_color = [0, 1, 0, 1]
                    else:
                        label.text = "Incorrect"
                        label.text_color = [1, 0, 0, 1]
                # QuestionResultLabel
                else:
                    label.text = f"Question {question_num}: "
            
            question_num += 1
