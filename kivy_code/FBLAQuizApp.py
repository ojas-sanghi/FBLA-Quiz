from datetime import datetime
from typing import List
from kivy.event import EventDispatcher

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.properties import NumericProperty, BooleanProperty, ListProperty

from .home import HomeScreen
from .mcq import MCQScreen
from .tf import TFScreen
from .blank import BlankScreen
from .matching import MatchingScreen
from .checkbox import CheckboxScreen
from .saq import SAQScreen
from .end import EndScreen

import quiz_generator

class ScreenManagement(ScreenManager):
    pass

class FBLAQuizApp(MDApp):
    # what screen we're on
    # 0-indexed, uses self.screens list
    screen_num = 0

    questions_correct = []

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        # load all files
        self.file_names = ["home", "mcq", "tf", "blank", "matching", "checkbox", "saq", "utils", "end"]
        for file in self.file_names:
            Builder.load_file("kivy_code/design/" + file + ".kv")

        self.questions = quiz_generator.get_questions(5)
        self.screens = [q.type for q in self.questions]


        MCQScreen.set_questions(MCQScreen, self.questions)
        TFScreen.set_questions(TFScreen, self.questions)
        BlankScreen.set_questions(BlankScreen, self.questions)
        MatchingScreen.set_questions(MatchingScreen, self.questions)
        CheckboxScreen.set_questions(CheckboxScreen, self.questions)
        SAQScreen.set_questions(SAQScreen, self.questions)


    def build(self):
        self.root = Builder.load_file("kivy_code/FBLAQuizApp.kv")
        
        # dark mode after 7 pm
        now = datetime.now()
        if now.hour >= 19:
            self.theme_cls.theme_style = "Dark" 
        else:
            self.theme_cls.theme_style = "Light"
        
        # self.root.current = "end"
        
    def has_answered_question(self):
        # don't go if the user hasn't answered
        # but we don't care about home and end screen
        if self.root.current_screen.name not in ["home", "end"]:
            
            if not self.root.current_screen.response:
                return False

            # for matching screen
            # ensure as many answers as there are words
            if self.root.current == "matching":
                if len(self.root.current_screen.response) != len(self.root.current_screen.words):
                    return False
        
        return True
        
    def next_screen(self):
        # if not self.has_answered_question():
        #     return

        # list has 5 items, so index cannot exceed 4
        if self.screen_num <= 4:
            self.root.current = self.screens[self.screen_num]
            self.screen_num += 1
        else:
            self.calculate_correct()
            self.root.current = "end"
    
    def calculate_correct(self):
        for s in self.screens:
            screen = self.root.get_screen(s)
            # append whether or not the user got it right
            if s == "checkbox":
                self.questions_correct.append(sorted(screen.response) == sorted(screen.answer))
            else:
                self.questions_correct.append(screen.response == screen.answer)
        
        EndScreen.set_response_data(EndScreen, self.questions_correct)
    
    def print_results(self):
        pass

    def matching_select(self, dropdown, answer_text):
        MatchingScreen.matching_select(self.root.current_screen, dropdown, answer_text)
        
if __name__ == "__main__":
    FBLAQuizApp().run()
