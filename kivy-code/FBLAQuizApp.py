
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.properties import StringProperty

from kivymd.app import MDApp

from matching import MatchingQuestion

class MCQScreen(Screen):
    question = StringProperty("this is a multiple choice question")

    option_1 = "option 1"
    option_2 = "option 2"
    option_3 = "option 3"
    option_4 = "option 4"

    def select(self, param):
        print(param)
        self.question = "cool MCQ question"

        print(self.ids)
    
    ###
    # for the dropdownmenu thing
    # maybe define that part in this file,
    # then add_widget(Builder.load_string)
    # or i guess Builder.load_file might work too

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
    question = "this is a multiple choice question"

    option_1 = "option 1"
    option_2 = "option 2"
    option_3 = "option 3"
    option_4 = "option 4"

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        Builder.load_file("utils.kv")
        Builder.load_file("mcq.kv")
        Builder.load_file("tf.kv")
        Builder.load_file("blank.kv")
        Builder.load_file("matching.kv")
        Builder.load_file("checkbox.kv")
        Builder.load_file("saq.kv")

        Clock.schedule_once(self._late_init)

    
    def _late_init(self, interval):
        pass

    def build(self):
        self.root = Builder.load_file("FBLAQuizApp.kv")
        self.theme_cls.theme_style = "Light"


    def select(self, param):
        print(param)
        self.question = "asdasda"
    
    def switch_match(self):
        self.root.current = "Matching"
        MatchingQuestion.do_stuff(self)
        
if __name__ == "__main__":
    FBLAQuizApp().run()
