from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDFabButton


KV = '''
MDScreen:
    md_bg_color: app.theme_cls.surfaceColor

    spacing: "32dp"
    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .3, "center_y": .5}

        MDButtonText:
            text: "Object Detection"

    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .51, "center_y": .5}

        MDButtonText:
            text: "Object Classification"

    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .71, "center_y": .5}

        MDButtonText:
            text: "Cursor Control"
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)


Example().run()