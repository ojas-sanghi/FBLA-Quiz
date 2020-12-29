from datetime import datetime

from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.progressbar import ProgressBar
from kivy.animation import Animation

import quiz_generator
from printer import Printer
from kivy.config import Config
from kivy.lang import Builder
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
from .dialogs import Dialogs

class FBLAQuizApp(MDApp):
    # what screen we're on
    # 0-indexed, uses self.screens list
    screen_num = 0

    questions_correct = []

    # colors we use 
    green_color = [0, 0.8, 0, 1]
    red_color = [1, 0.2, 0.2, 1]
    yellow_color = [1, .75, 0, 1]

    sm: ScreenManager

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        # don't make red circles on RMB click
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

        # load all files
        self.file_names = ["home", "mcq", "tf", "blank", "matching", "checkbox", "saq", "utils", "dialogs", "end"]
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

    def build(self):
        self.root = Builder.load_file("kivy_code/FBLAQuizApp.kv")
        self.sm = self.root.ids.sm
        
        # dark mode after 7 pm, before 6 am
        now = datetime.now()
        if now.hour >= 19 or now.hour <= 6:
            self.theme_cls.theme_style = "Dark" 
        else:
            self.theme_cls.theme_style = "Light"

        # self.theme_cls.theme_style = "Light"
        # self.sm.current = "blank"

    def has_answered_question(self):
        # don't go if the user hasn't answered
        # but we don't care about home and end screen
        if self.sm.current_screen.name not in ["home", "end"]:
            
            if not self.sm.current_screen.question.response:
                return False

            # for matching screen
            # ensure as many answers as there are words
            if self.sm.current == "matching":
                if len(self.sm.current_screen.question.response) != len(self.sm.current_screen.words):
                    return False
        
        return True
    
    def submit_answer(self):
        d = Dialogs()
        d.disable_others(self.sm.current_screen)
        
        if not self.has_answered_question():
            d.incomplete_dialog.open()
        elif self.sm.current_screen.question.is_correct():
            d.correct_dialog.open()
        else:
            d.incorrect_dialog.open()
            
    def next_screen(self):
        self.sm.transition.direction = "left"
        bar: ProgressBar = self.root.ids.progress_bar

        # list has 5 items, so index cannot exceed 4
        if self.screen_num <= 4:
            self.sm.current = self.screens[self.screen_num]
            self.screen_num += 1

            bar.opacity = 1
            anim = Animation(value = self.screen_num * 20, t = "out_cubic")
            anim.start(bar)
            
        else:
            bar.opacity = 0
            self.calculate_correct()
            self.sm.current = "end"


    def calculate_correct(self):
        for s in self.screens:
            screen = self.sm.get_screen(s)
            self.questions_correct.append(screen.question.is_correct())

        EndScreen.set_response_data(EndScreen, self.questions_correct)
    
    def print_results(self):
        p = Printer(self.questions, self.questions_correct)
        p.print()

    ######################################
    # utility functions screens/widgets
    #######################################

    def matching_select(self, dropdown):
        MatchingScreen.matching_select(self.sm.current_screen, dropdown)
    
    # only expand if previous dropdown is selected
    def matching_previous_selected(self, drop_menu):
        dropdown_elements = self.sm.current_screen.ids.option_grid.children
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
