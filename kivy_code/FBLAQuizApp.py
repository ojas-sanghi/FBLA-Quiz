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
    yellow_color = [1, 0.75, 0, 1]

    sm: ScreenManager

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        # don't make red circles on RMB click
        Config.set("input", "mouse", "mouse,multitouch_on_demand")

        # load all files
        self.file_names = [
            "home",
            "mcq",
            "tf",
            "blank",
            "matching",
            "checkbox",
            "saq",
            "utils",
            "dialogs",
            "end",
        ]
        for file in self.file_names:
            Builder.load_file("kivy_code/design/" + file + ".kv")

        self.reset()

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

    def reset(self):
        # generate 5 random questions
        self.questions = quiz_generator.get_questions(5)
        self.screens = [q.type for q in self.questions]

        # set details for the questions in each screen
        for s in [
            MCQScreen,
            TFScreen,
            BlankScreen,
            MatchingScreen,
            CheckboxScreen,
            SAQScreen,
        ]:
            s.set_questions(s, self.questions)

        self.screen_num = 0
        self.questions_correct = []

    def restart(self):
        self.reset()
        self.root.ids.progress_bar.value = 0

        self.sm.current = "home"

    def has_answered_question(self):
        # don't go if the user hasn't answered
        # but we don't care about home and end screen
        if self.sm.current_screen.name not in ["home", "end"]:

            if not self.sm.current_screen.question.response:
                return False

            # for matching screen
            # ensure as many answers as there are words
            if self.sm.current == "matching":
                # get the list of answers {'Hedgehog': 'Pick Option', 'Horse': 'B'} -> ['Pick Option', 'B']
                # if any of then are more than 1 letter, then they haven't responded
                for r in self.sm.current_screen.question.response.values():
                    if len(r) > 1:
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

            # show submit button every screen
            # gets hidden after restart so we need to show it again
            s = self.sm.current_screen.ids.submit_btn
            s.disabled = False
            s.opacity = 1

            # increment counter
            self.screen_num += 1

            # make sure bar is visible, and smoothly animate its value increasing
            bar.opacity = 1
            anim = Animation(value=self.screen_num * 20, t="out_cubic")
            anim.start(bar)

        else:
            bar.opacity = 0
            self.calculate_correct()
            self.sm.current = "end"

    def calculate_correct(self):
        # don't calculate anything if we're at the starting and ending screens
        if self.sm.current in ["home", "end"]:
            return

        for s in self.screens:
            screen = self.sm.get_screen(s)
            self.questions_correct.append(screen.question.is_correct())

        for s in self.sm.screens:
            if s.name == "end":
                s.set_response_data(self.questions_correct)

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
