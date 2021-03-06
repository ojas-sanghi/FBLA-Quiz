from functools import partial
from question import Question

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty, ListProperty

from kivy.factory import Factory


class MatchingScreen(Screen):
    question: Question
    text = StringProperty("Matching question")
    options = ListProperty(["option 1", "option 2", "option 3"])
    words = ListProperty(["word 1", "word 2", "word 3", "word 4", "word 5"])

    times_called = 0

    def update_dropdown_item_size(self, dropdown_item, dropdown_buttons, *largs):
        # set button size to the dropdown_item size
        # subtract 2 from width to make it look better
        for drop_button in dropdown_buttons:
            drop_button.size = dropdown_item.size
            drop_button.size[0] -= 2

        # increment times_called
        # cancel event once called twice
        self.times_called += 1
        if self.times_called == 2:
            Clock.unschedule(self.update_event)
            self.times_called = 0

    # when we select a choice, we need to change the size of the "MyDropDownButton"s
    # to the size of the MDDropDownItem otherwise they look weird
    # this is accomplished by first going through the tree to get the relevant items
    # then we pass that to update_dropdown_item_size()
    # which is called twice over 0.002s
    def matching_select(self, dropdown):
        self.times_called = 0

        option_grid_children = self.ids.option_grid.children
        dropdown_item = None
        dropdown_buttons = None

        my_label_class = Factory.classes["MyLabel"]["cls"]
        my_dropdown_class = Factory.classes["MyDropDown"]["cls"]
        word: str = ""

        # construct dictionary of answers
        # used for answer validation
        # {"pig": "A"}
        for item in option_grid_children:
            # get word
            if type(item) == my_label_class:
                word = item.text
            # get option (A, B, C)
            if type(item) == my_dropdown_class:
                dropdown_item = item.ids.btn
                self.question.response[word] = dropdown_item.text

                # dropdown.children[0] gets a GridLayout (used internally)
                # doing the .children actually gets the "MyDropDownButton"s
                dropdown_buttons = dropdown.children[0].children

        self.update_event = Clock.schedule_interval(
            partial(self.update_dropdown_item_size, dropdown_item, dropdown_buttons),
            0.001,
        )

    def set_questions(self, qs: list):
        self.questions = qs

    def on_pre_enter(self):
        self.reset()
        q_num = 0
        for q in self.questions:
            if q.type == "matching":
                q_num = self.questions.index(q) + 1

                self.question = q
                self.text = q.text + f" (Question {q_num}/5)"
                self.options = q.options
                self.words = q.words

                self.question.response = {}

    def reset(self):
        self.ids.drop1.ids.btn.text = "Pick Option"
        self.ids.drop2.ids.btn.text = "Pick Option"
        self.ids.drop3.ids.btn.text = "Pick Option"
        self.ids.drop4.ids.btn.text = "Pick Option"
        self.ids.drop5.ids.btn.text = "Pick Option"
