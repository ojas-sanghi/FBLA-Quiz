from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, ListProperty


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
                        label.text_color = [0, 0.8, 0, 1]
                    else:
                        label.text = "Incorrect"
                        label.text_color = [1, 0.2, 0.2, 1]
                # QuestionResultLabel
                else:
                    label.text = f"Question {question_num}: "

            question_num += 1

    def on_enter(self, *args):
        progress_circle = self.ids.progress
        progress_circle.current_percent = self.total_correct
    
    # called when you exit the screen, rather than when you enter it
    def reset(self):
        self.questions_correct = [False, False, False, False, False]
        self.total_correct = 0

        self.ids.progress.current_percent = 0

        self.ids.correct1.text = "Incorrect"
        self.ids.correct2.text = "Incorrect"
        self.ids.correct3.text = "Incorrect"
        self.ids.correct4.text = "Incorrect"
        self.ids.correct5.text = "Incorrect"