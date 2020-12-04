from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout

from functools import partial

class MatchingScreen(Screen):

    times_called = 0

    def update_dropdown_item_size(self, dropdown_item, dropdown_buttons, *largs):
        # set button size to the dropdown_item size
        # subtract 2 from width to make it look better
        for drop_button in dropdown_buttons:
            drop_button.size = dropdown_item.size
            drop_button.size[0] -= 2

        # increment times called
        # cancel event once called 10 times
        self.times_called += 1
        if self.times_called == 10:
            self.update_event.cancel()


    # when we select a choice, we need to change the size of the "MyDropDownButton"s
    # to the size of the MDDropDownItem otherwise they look weird
    # this is accomplished by first going through the tree to get the relevant items
    # then we pass that to the upadte_dropdown_item_size function
    # which is called 10 times over 1 second
    # we have to do it repeatedly since doing it once or after the next frame doesn't work for some reason
    def matching_select(self, dropdown):
        dropdown_grid = self.ids.option_grid.children

        dropdown_item = None
        dropdown_buttons = None

        for obj in dropdown_grid:
            # make sure we're only getting the DropDowns
            if isinstance(obj, MDFloatLayout):
                dropdown_item = obj.children[0]

                # dropdown.children[0] gets a GridLayout
                # because the dropdown uses a gridlayout internally
                # doing the .children actually gets the "MyDropDownButton"s
                dropdown_buttons = dropdown.children[0].children

        self.update_event = Clock.schedule_interval(partial(self.update_dropdown_item_size, dropdown_item, dropdown_buttons), 0.1)
