from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

from kivymd_extensions.akivymd.uix.dialogs import AKAlertDialog

class Dialogs(Screen):
    current: Screen
    app: MDApp

    dialog: AKAlertDialog

    def __init__(self, **kw):
        super().__init__(**kw)

    def correct(self):
        dialog = AKAlertDialog(
            header_icon="check-circle-outline", header_bg=[0, 0.7, 0, 1]
        )
        content = Factory.CorrectDialog()
        content.ids.button.bind(on_release=dialog.dismiss)
        dialog.content_cls = content
        dialog.open()

    def incorrect(self):
        dialog = AKAlertDialog(
            header_icon="close-circle-outline", header_bg=[0.9, 0, 0, 1]
        )
        content = Factory.IncorrectDialog()
        content.ids.button.bind(on_release=dialog.dismiss)
        dialog.content_cls = content
        dialog.open()

    def incomplete(self):
        dialog = AKAlertDialog(
            header_icon="exclamation",
            header_bg=[1, 0.75, 0, 1],
        )
        self.dialog = dialog
        content = Factory.IncompleteDialog()
        content.ids.button.bind(on_release=self.incomplete_dialog_callback)
        dialog.content_cls = content
        dialog.open()
    
    def incomplete_dialog_callback(self, *args, **kwargs):
        self.dialog.dismiss()
        self.enable_others()
    
    def disable_others(self, app: MDApp, current: Screen):
        self.app = app
        self.current = current
        
        ids = self.current.ids
        submit = ids.submit_btn
        previous = ids.prev_btn

        submit.disabled = True
        submit.opacity = 0

        previous.disabled = True
        previous.opacity = 0

    def enable_others(self):
        ids = self.current.ids
        submit = ids.submit_btn
        previous = ids.prev_btn

        submit.disabled = False
        submit.opacity = 1

        previous.disabled = False
        previous.opacity = 1
        self.app.check_prev_btn_opacity()