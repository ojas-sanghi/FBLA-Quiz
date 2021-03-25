from typing import List

import platform

from dominate import tags
from question import Question
import tempfile
import dominate
from dominate.tags import *
from dominate.util import raw, text

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

        self.temphtml = tempfile.mktemp(".html")

        # make a new html doc
        doc = dominate.document()

        question_num = 1

        show_hide_code = "var x = document.getElementById('{}'); var button = document.getElementById('{}'); if (x.style.visibility === 'hidden') {{ x.style.visibility = 'visible'; button.innerText = 'Hide' }} else {{ x.style.visibility = 'hidden'; button.innerText = 'Show'; }}"
        
        hide_buttons_code = "var self = document.getElementById('hideAllButtons'); var hiding = true; if (self.textContent == '-- Buttons visible; press to hide all --') { hiding = true; self.textContent = '-- Buttons hidden --'; } else { hiding = false;  self.textContent = '-- Buttons visible; press to hide all --'; } for (var i = 1; i <= 6 ; i++) { var user = document.getElementById('userAnsButton' + i); var correct = document.getElementById('correctAnsButton' + i); var result = document.getElementById('resultButton' + i); if (hiding) { console.log('hiding'); user.style.display = 'none'; correct.style.display = 'none'; result.style.display = 'none'; } else { console.log('showing'); self.textContent = '-- Buttons visible; press to hide all --'; user.style.display = ''; correct.style.display = ''; result.style.display = ''; } } "


        with doc.head:
            title("FBLA Quiz Results", style="font-family: Georgia")
            raw("<meta charset='utf-8'>")
            link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/litera/bootstrap.min.css")
            link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css")
            # link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js")
        
        with doc:
            with div(cls="container", style="font-family: Georgia"):
                h1("FBLA Quiz Results")
                h2(f"Total Correct: {self.num_correct}/{len(self.questions)}")

                button("-- Buttons visible; press to hide all --", id="hideAllButtons", cls="waves-effect waves-teal btn-flat", onclick=hide_buttons_code)

                br()

                for question in self.questions:
                    with div(style=f"margin-top: -19px", title=f"Q{question_num}"):
                        if question_num != 1:
                            br()
                        hr()

                        h3(u(f"Question {question_num}"))
                        h4(question.text)

                        br()

                        if question.type in ["mcq", "tf", "checkbox"]:
                            # split list into two
                            first_half_options = question.options[
                                : len(question.options) // 2
                            ]
                            second_half_options = question.options[
                                len(question.options) // 2 :
                            ]

                            # two columns for options
                            with div(cls="row"):
                                with div(cls="col s2"):
                                    with table(cls="centered", style="font-size: 1rem"):
                                        with tbody():
                                            with tr():
                                                for option in first_half_options:
                                                    td(option)
                                            with tr():
                                                for option in second_half_options:
                                                    td(option)
                                with div(cls="col s10"):
                                    p("")

                        # two columns for matching; one with options, one with words
                        # mimics the actual question screen so it's familiar
                        if question.type == "matching":
                            with div(cls="row"):
                                with div(cls="col s2"):
                                    with table(cls="centered", style="font-size: 1rem"):
                                        with tbody():
                                            for i in range(0, 3):
                                                with tr():
                                                    td(question.words[i])
                                                    td(question.options[i])
                                            for i in range(3, 5):
                                                with tr():
                                                    td(question.words[i])
                                                    td("")
                                with div(cls="col s10"):
                                    p("")

                        # prints out what the user's answer is and what the correct answer is
                        response = question.response
                        answer = question.answer

                        # specially formatted response string
                        if question.type in ["checkbox"]:
                            response = ", ".join(question.response)
                            answer = ", ".join(question.answer)

                        if question.type == "matching":
                            # reverse response list to make it in order of the questions
                            # we need to do this because of the way values are added to the dictionary initially
                            response = list(reversed(response.values()))
                            response = ", ".join(response)

                            answer = ", ".join(answer.values())

                        # line goes before "your answer" etc
                        # looks odd for blank and saq so not done for those
                        # if question.type not in ["blank", "saq"]:
                        #     p("-----------------------------------")

                        style_str = (
                            "color: green" if question.is_correct() else "color: chocolate"
                        )

                        with div(cls="row"):
                            with div(cls="col s2"):
                                button("Show", id="userAnsButton" + str(question_num), cls="waves-effect waves-light btn-small", onclick=show_hide_code.format("userAnswer" + str(question_num), "userAnsButton" + str(question_num)))
                                
                            with div(cls="col s10 pull-s5"):
                                p("Your answer: ", span(response, id="userAnswer" + str(question_num), style=style_str + "; visibility:hidden"))

                        with div(cls="row"):
                            with div(cls="col s2"):
                                button("Show", id="correctAnsButton" + str(question_num), cls="waves-effect waves-light btn-small", onclick=show_hide_code.format("correctAnswer" + str(question_num), "correctAnsButton" + str(question_num)))
                            
                            with div(cls="col s10 pull-s5"):
                                p("Correct answer: ", span(answer, id="correctAnswer" + str(question_num), style="color:green; visibility:hidden"))
                        
                        with div(cls="row"):
                            with div(cls="col s2"):
                                button("Show", id="resultButton" + str(question_num), cls="waves-effect waves-light btn-small", onclick=show_hide_code.format("resultText" + str(question_num), "resultButton" + str(question_num)))
                            
                            with div(cls="col s10 pull-s5"):
                                if question.is_correct():
                                    b(p("Result:", span("Correct", id="resultText" + str(question_num), style="color: green; visibility:hidden")))
                                else:
                                    b(p("Result:", span("Incorrect", id="resultText" + str(question_num),style="color: red; visibility:hidden")))

                    question_num += 1
            
        with open(self.temphtml, "w") as f:
            f.write(doc.render())

        # load html code into HTML object as a string
        # then convert it to a pdf and write it to the temp file created
        weasyprint.HTML(string=doc.render()).write_pdf(self.filename)

    def print(self):
        self.construct_file()

        if platform.system() == "Windows":
            # subprocess.call(("start", self.filename), shell=True)
            subprocess.call(("start", self.temphtml), shell=True)

        elif platform.system() == "Linux":
            subprocess.call(("xdg-open", self.filename))

        elif platform.system() == "Darwin":
            subprocess.call(("open", self.filename))


# fmt: off
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
    questions[2].response = {"hedgehog": "B", "horse": "A", "zebra": "A", "lion": "B", "pig": "C"}
    questions[3].response = "business"
    questions[4].response = "False"
    questions[5].response = "future smart"

    correct_list = [True, False, False, True, False, False]

    printer = Printer(questions, correct_list)
    printer.print()
