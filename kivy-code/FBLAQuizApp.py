from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

from kivymd.app import MDApp
# from kivymd.uix.button import MDRaisedButton

from mcq import MCQScreen
from tf import TFScreen
from blank import BlankScreen
from matching import MatchingScreen
from checkbox import CheckboxScreen
from saq import SAQScreen

    
###
# for the MDDropdownMenu thing
# maybe define that part in this file,
# then add_widget(Builder.load_string)
# or i guess Builder.load_file might work too

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
            Builder.load_file(file)

        Clock.schedule_once(self._late_init)

    
    def _late_init(self, interval):
        pass

    def build(self):
        self.root = Builder.load_file("FBLAQuizApp.kv")
        self.theme_cls.theme_style = "Dark"


    def select(self, param):
        print(param)
        self.question = "asdasda"
    
    def matching_select(self, dropdown):
        MatchingScreen.matching_select(self.root.current_screen, dropdown)
        
if __name__ == "__main__":
    FBLAQuizApp().run()
