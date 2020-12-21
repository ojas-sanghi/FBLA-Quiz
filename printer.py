from typing import List

import platform
from question import Question
import tempfile
import dominate
from dominate.tags import *

import weasyprint
import subprocess

class Printer:
    questions: List[Question]
    correct_list: List[bool]
    filename: str
    num_correct: int

    def __init__(self, questions, correct_list) -> None:
        self.questions = questions
        self.correct_list = correct_list
        self.num_correct = self.correct_list.count(True)


    def construct_file(self):
        # make a temporary file
        # this is where we will write our output
        self.filename = tempfile.mktemp(".pdf")

        # make a new html doc
        doc = dominate.document(title="FBLA Quiz Results")

        question_num = 1

        with doc:
            h1("FBLA Quiz Results")
            h2(f"Total Correct: {self.num_correct}/{len(self.questions)}")

            br()

            for question in self.questions:
                with div(style=f"margin-top: -19px", title=f"Q{question_num}"):
                    if question_num != 1:
                        br()
                    hr()

                    h3(u(f"Question {question_num}"))
                    h4(question.text)

                    if question.type in ["mcq", "tf", "checkbox"]:
                        u("Options:")
                        for option in question.options:
                            with ul():
                                # green for the answer
                                if option == question.answer:
                                    li(p(option, style="color: green"))
                                    continue
                                # yellow for wrong user choice
                                if option == question.response:
                                    li(p(option, style="color: chocolate"))
                                    continue
                                li(p(option))
                        

                    if question.type == "matching":
                        with div(style="display: flex"):
                            with div(style="flex: 50%"):
                                with ul():
                                    [li(p(word)) for word in question.words]
                            with div(style="flex: 50%"):
                                with ul():
                                    [p(option) for option in question.options]
                            
                        
                    # for checkbox and matching, the previous part just prints out options
                    # this also prints out what the user's answer is and what the correct answer is
                    if question.type in ["blank", "saq", "checkbox", "matching"]:

                        response = question.response
                        answer = question.answer
                        # specially formatted response string

                        if question.type in ["checkbox"]:
                            response = ", ".join(question.response)
                            answer = ", ".join(question.answer)
                        
                        if question.type == "matching":
                            response = ", ".join(response.values())
                            answer = ", ".join(answer.values())

                        # line goes before "your answer" etc
                        if question.type in ["checkbox", "matching"]: p("-----------------------------------")
                        if question.is_correct():
                            p("Your answer: ", span(response, style="color:green"))
                        else:
                            p("Your answer: ", span(response, style="color:chocolate"))
                        p("Correct answer: ", span(answer, style="color:green"))

                    else:
                        # line only goes before "result"
                        # done for mcq and tf
                        p("-----------------------------------")
                    

                    # color-coded correct/incorrent
                    if question.is_correct():
                        p("Result:", span("Correct", style="color: green"))
                    else:
                        p("Result:", span("Incorrect", style="color: red"))
                    
                question_num += 1


        with open("test.html", "w") as f:
            f.write(doc.render())
        # load html code into HTML object as a string
        # then convert it to a pdf and write it to the temp file created
        weasyprint.HTML(string=doc.render()).write_pdf(self.filename)


    def print(self):
        self.construct_file()
        print(self.filename)

        if platform.system() == "Windows":
            subprocess.call(('start', self.filename), shell=True)
        
        elif platform.system() == "Linux":
            subprocess.call(('xdg-open', self.filename))

        elif platform.system() == "Darwin":
            subprocess.call(('open', self.filename))

    
if __name__ == "__main__":
    questions = [
        Question({'id': 4, 'type': 'checkbox', 'question': 'Which of the following are true about FBLA? (Choose all that apply)', 'options': ['has BAA', 'is college program', 'is high school program', 'costs $20,000'], 'answer': ['has BAA', 'is high school program']}),
        Question({'id': 23, 'type': 'saq', 'question': 'What is the full form of the BAA?', 'answer': 'business achievement awards'}),
        Question({'id': 21, 'type': 'matching', 'question': 'Match the animals to their diets', 'options': ['A) carnivore', 'B) omnivore', 'C) herbivore'], 'words': ['pig', 'lion', 'zebra', 'horse', 'hedgehog'], 'answer': {'pig': 'B', 'lion': 'A', 'zebra': 'C', 'horse': 'C', 'hedgehog': 'B'}}),
        Question({'id': 32, 'type': 'blank', 'question': 'FBLA stands for: Future ________ Leaders of America', 'answer': 'business'}),
        Question({'id': 37, 'type': 'tf', 'question': 'True/False: FBLA is goated', 'options': ['True', 'False'], 'answer': 'True'}),
        Question({'id': 0, 'type': 'mcq', 'question': 'What does FBLA stand for?', 'options': ['future dumb', 'future smart', 'future scammers', 'future leaders'], 'answer': 'future leaders'})
    ]
    questions[0].response = ["has BAA", "is high school program"]
    questions[1].response = "business accolades"
    questions[2].response = {'pig': 'C', 'lion': 'B', 'zebra': 'A', 'horse': 'A', 'hedgehog': 'B'}
    questions[3].response = "business"
    questions[4].response = "False"
    questions[5].response = "future smart"

    correct_list = [True, True, False, True, False, True]

    printer = Printer(questions, correct_list)
    printer.print()