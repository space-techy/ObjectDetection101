from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.behaviors.hover_behavior import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class HoverBox(RelativeLayout, HoverBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expanded = False

        # Small box
        self.small_box = Label(text='Hover me', size_hint=(None, None), size=(100, 100))
        self.add_widget(self.small_box)

        # Grid layout for expanded view
        self.grid_layout = GridLayout(cols=2)
        self.image = Image(source='./image.png')
        self.info_label = Label(text='This is some information about the image.')
        self.grid_layout.add_widget(self.image)
        self.grid_layout.add_widget(self.info_label)

    def on_enter(self, *args):
        if not self.expanded:
            self.remove_widget(self.small_box)
            self.add_widget(self.grid_layout)
            self.expanded = True

    def on_leave(self, *args):
        if self.expanded:
            self.remove_widget(self.grid_layout)
            self.add_widget(self.small_box)
            self.expanded = False

class HoverBoxApp(App):
    def build(self):
        root = RelativeLayout()
        hover_box = HoverBox()
        root.add_widget(hover_box)
        return root

if __name__ == '__main__':
    HoverBoxApp().run()