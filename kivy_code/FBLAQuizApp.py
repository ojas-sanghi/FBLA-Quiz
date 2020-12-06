import random
from datetime import datetime

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from .mcq import MCQScreen
from .tf import TFScreen
from .blank import BlankScreen
from .matching import MatchingScreen
from .checkbox import CheckboxScreen
from .saq import SAQScreen

import quiz_generator

class ScreenManagement(ScreenManager):
    pass

class FBLAQuizApp(MDApp):
    question = "this is a multiple choice question"

    option_1 = "option 1"
    option_2 = "option 2"
    option_3 = "option 3"
    option_4 = "option 4"


    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        file_names = ["utils.kv", "mcq.kv", "tf.kv", "blank.kv", "matching.kv", "checkbox.kv", "saq.kv"]
        for file in file_names:
            Builder.load_file("kivy_code/" + file)
        
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
        # self.next_screen()
        
        # dark mode after 7 pm
        now = datetime.now()
        if now.hour >= 19:
            self.theme_cls.theme_style = "Dark" 
        else:
            self.theme_cls.theme_style = "Light"
        

    def next_screen(self):
        # remove this later when we implement a congrats screen
        # we finished all the questions, nowhere to go next
        try:
            self.screens.remove(self.root.current)
        except:
            # TODO: move to congrats screen
            pass

        print(len(self.screens))
    
        if len(self.screens) >= 1:
            next_screen = random.choice(self.screens)
            self.root.current = next_screen
            print(next_screen)
        else:
            pass
    
    def matching_select(self, dropdown, answer_text):
        MatchingScreen.matching_select(self.root.current_screen, dropdown, answer_text)
        
if __name__ == "__main__":
    FBLAQuizApp().run()
