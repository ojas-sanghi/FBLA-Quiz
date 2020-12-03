
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

from kivymd.app import MDApp

from matching import MatchingQuestion

class MCQScreen(Screen):
    pass

class TFScreen(Screen):
    pass

class BlankScreen(Screen):
    pass

class MatchingScreen(Screen):
    pass

class CheckboxScreen(Screen):
    pass

class SAQScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class FBLAQuizApp(MDApp):
    question = ""

    option_1 = ""
    option_2 = ""
    option_3 = ""
    option_4 = ""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        Builder.load_file("mcq.kv")
        Builder.load_file("tf.kv")
        Builder.load_file("blank.kv")
        Builder.load_file("matching.kv")
        Builder.load_file("checkbox.kv")
        Builder.load_file("saq.kv")

        Clock.schedule_once(self._late_init)
    
    def _late_init(self, interval):
        print("hiii")

    
    def build(self):
        self.set_text()

        self.root = Builder.load_file("FBLAQuizApp.kv")
        self.theme_cls.theme_style = "Light"
    
    def set_text(self):
        self.question = "this is a multiple choice question"
        self.option_1 = "option 1"
        self.option_2 = "option 2"
        self.option_3 = "option 3"
        self.option_4 = "option 4"

    def select(self, param):
        print(param)
    
    def switch_match(self):
        self.root.current = "Matching"
        MatchingQuestion.do_stuff()

# see https://github.com/kivymd/KivyMD/issues/511 to maybe fix MDDropdownMenu
# maybe ask in main kivychat why the dropdown thing is being weird



# make a kivyquestion.kv
# in each relative .py file (matching.py etc)
# set the details of that kivyquestion
# which will set its own details on runtime

# figure out how to make it work - .py file? .kv file hooks into .py file of same name to set details?
# maybe in respective questions we just set a kv string 

if __name__ == "__main__":
    FBLAQuizApp().run()
