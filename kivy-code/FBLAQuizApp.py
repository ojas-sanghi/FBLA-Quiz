
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition

from kivymd.app import MDApp


class MCQScreen(Screen):
    pass

class TFScreen(Screen):
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
        self.question = "fbla full form"
        self.option_1 = "future dumb"
        self.option_2 = "future smart"
        self.option_3 = "future scammers"
        self.option_4 = "future leaders"

    def select(self, param):
        print(param)

if __name__ == "__main__":
    FBLAQuizApp().run()
