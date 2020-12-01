
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.app import MDApp

class MCQScreen(Screen):
    pass

class TFScreen(Screen):
    pass

class BlankScreen(Screen):
    pass

class MatchingScreen(Screen):
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
        super(FBLAQuizApp, self).__init__(**kwargs)

    
    def build(self):
        self.set_text()

        self.root = Builder.load_file("mcq.kv")
        self.theme_cls.theme_style = "Light"
    
    def set_text(self):
        self.question = "this is a multiple choice question"
        self.option_1 = "option 1"
        self.option_2 = "option 2"
        self.option_3 = "option 3"
        self.option_4 = "option 4"

    def select(self, param):
        print(param)

if __name__ == "__main__":
    FBLAQuizApp().run()
