from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd_extensions.akivymd.uix.dialogs import AKAlertDialog

class Dialogs(Screen):
    submit: MDRaisedButton

    correct_dialog: AKAlertDialog
    incorrect_dialog: AKAlertDialog    
    incomplete_dialog: AKAlertDialog

    def __init__(self, **kw):
        super().__init__(**kw)

        # on initialization, make the dialogs and store them in attributes
        self.correct()
        self.incorrect()
        self.incomplete()

    def correct(self):
        dialog = AKAlertDialog(
            header_icon="check-circle-outline", 
            header_bg=[0, 0.8, 0, 1], 
        )
        content = Factory.CorrectBox()
        content.ids.button.bind(on_release=dialog.dismiss)
        dialog.content_cls = content

        self.correct_dialog = dialog

    def incorrect(self):
        dialog = AKAlertDialog(
            header_icon="close-circle-outline", 
            header_bg=[1, 0.2, 0.2, 1], 
        )
        content = Factory.IncorrectBox()
        content.ids.button.bind(on_release=dialog.dismiss)
        dialog.content_cls = content

        self.incorrect_dialog = dialog

    def incomplete(self):
        dialog = AKAlertDialog(
            header_icon="exclamation", 
            header_bg=[1, 0.75, 0, 1],
        )
        content = Factory.IncompleteBox()
        content.ids.button.bind(on_release=self.incomplete_dialog_callback)
        dialog.content_cls = content

        self.incomplete_dialog = dialog
    
    def incomplete_dialog_callback(self, *args):
        self.incomplete_dialog.dismiss()
        self.enable_others()
    
    def disable_others(self, current: Screen):
        self.submit = current.ids.submit_btn
        
        self.submit.disabled = True
        self.submit.opacity = 0

    # disable is always called first
    # enabled is only called for the incomplete popup
    # so the button will remain the same
    def enable_others(self):
        self.submit.disabled = False
        self.submit.opacity = 1