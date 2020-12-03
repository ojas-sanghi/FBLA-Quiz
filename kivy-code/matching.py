from kivymd.app import MDApp

class MatchingQuestion(MDApp):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def do_stuff(self):
        print("yo")

        print(self.get_running_app())
        print(self.root)

        print(self.root.ids)
        print(self.root.screen_names)

        print(self.root.current_screen)
