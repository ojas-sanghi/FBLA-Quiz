from datetime import datetime

import quiz_generator
from printer import Printer
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.factory import Factory
from kivymd.app import MDApp

from .blank import BlankScreen
from .checkbox import CheckboxScreen
from .end import EndScreen
from .home import HomeScreen
from .matching import MatchingScreen
from .mcq import MCQScreen
from .saq import SAQScreen
from .tf import TFScreen
from .utils import Dialogs

class ScreenManagement(ScreenManager):
    pass

class FBLAQuizApp(MDApp):
    # what screen we're on
    # 0-indexed, uses self.screens list
    screen_num = 0

    questions_correct = []

    # colors we use 
    green_color = [0, 0.8, 0, 1]
    red_color = [1, 0.2, 0.2, 1]

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        # don't make red circles on RMB click
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

        # load all files
        self.file_names = ["home", "mcq", "tf", "blank", "matching", "checkbox", "saq", "utils", "end"]
        for file in self.file_names:
            Builder.load_file("kivy_code/design/" + file + ".kv")

        # generate 5 random questions
        self.questions = quiz_generator.get_questions(5)
        self.screens = [q.type for q in self.questions]

        # set details for the questions in each respective screen
        MCQScreen.set_questions(MCQScreen, self.questions)
        TFScreen.set_questions(TFScreen, self.questions)
        BlankScreen.set_questions(BlankScreen, self.questions)
        MatchingScreen.set_questions(MatchingScreen, self.questions)
        CheckboxScreen.set_questions(CheckboxScreen, self.questions)
        SAQScreen.set_questions(SAQScreen, self.questions)

        # TODO:
        # WRAP LABELS IN KIVY????
        # add questions in questions.json

        # verify printing mac

        # endgame challenges: 
        # keep progressbar, move just the question
        # make html look prettier
        


    def build(self):
        self.root = Builder.load_file("kivy_code/FBLAQuizApp.kv")
        
        # dark mode after 7 pm, before 6 am
        now = datetime.now()
        if now.hour >= 19 or now.hour <= 6:
            self.theme_cls.theme_style = "Dark" 
        else:
            self.theme_cls.theme_style = "Light"

        # self.theme_cls.theme_style = "Light"
        # self.root.current = "end"

    def has_answered_question(self):
        # don't go if the user hasn't answered
        # but we don't care about home and end screen
        if self.root.current_screen.name not in ["home", "end"]:
            
            if not self.root.current_screen.question.response:
                return False

            # for matching screen
            # ensure as many answers as there are words
            if self.root.current == "matching":
                if len(self.root.current_screen.question.response) != len(self.root.current_screen.words):
                    return False
        
        return True
    
    def submit_answer(self):
        d = Dialogs()
        d.disable_others(self, self.root.current_screen)
        
        if not self.has_answered_question():
            d.incomplete()
        elif self.root.current_screen.question.is_correct():
            d.correct()
        else:
            d.incorrect()
            
    def next_screen(self):
        self.root.transition.direction = "left"
        # list has 5 items, so index cannot exceed 4
        if self.screen_num <= 4:
            self.root.current = self.screens[self.screen_num]
            self.screen_num += 1

            progress_value = self.screen_num * 20
            self.root.current_screen.ids.progress_bar.value = progress_value

        else:
            self.calculate_correct()
            self.root.current = "end"


    def calculate_correct(self):
        for s in self.screens:
            screen = self.root.get_screen(s)
            self.questions_correct.append(screen.question.is_correct())

        EndScreen.set_response_data(EndScreen, self.questions_correct)
    
    def print_results(self):
        p = Printer(self.questions, self.questions_correct)
        p.print()

    ######################################
    # utility functions screens/widgets
    #######################################

    def matching_select(self, dropdown):
        MatchingScreen.matching_select(self.root.current_screen, dropdown)
    
    # only expand if previous dropdown is selected
    def matching_previous_selected(self, drop_menu):
        dropdown_elements = self.root.current_screen.ids.option_grid.children
        dropdown_elements = list(reversed(dropdown_elements))

        # construct list of MyDropDowns
        dropdowns = []
        for element in dropdown_elements:
            if type(element) == Factory.classes["MyDropDown"]["cls"]:
                dropdowns.append(element)

        index = dropdowns.index(drop_menu)
        previous = dropdowns[index - 1]

        # if the first dropdown itself is checking, then return true
        # the first dropdown needs to be able to select an option
        if index == 0:
            return True

        # should be A/B/C, "pick option" is the default
        return previous.ids.btn.text != "Pick Option"
        

if __name__ == "__main__":
    FBLAQuizApp().run()
