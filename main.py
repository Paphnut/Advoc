from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class Advoc(MDApp):
    def build(self):
        return MDLabel(text="Hello, Advoc!", halign="center")


Advoc().run()