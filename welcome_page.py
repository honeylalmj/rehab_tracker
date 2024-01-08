from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from login_page import LoginPage
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder

KV = '''
FloatLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1.0  # White background color (RGBA values)
        Rectangle:
            pos: self.pos
            size: self.size
    MDLabel:
        text: "REHAB TRACKER"
        theme_text_color: "Custom"
        text_color: "blue"
        pos_hint: {"center_x": 0.6, "center_y": 0.6}
        size_hint: 0.3, 0.1
    MDRaisedButton:
        text: "Proceed"
        md_bg_color: "green"
        pos_hint: {"center_x": 0.49, "center_y": 0.45}
        size_hint: 0.05, 0.05
        on_press: app.login()
'''

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return self.screen

    def login(self):
        self.stop()
        LoginPage().run()


if __name__ == "__main__":
    MainApp().run()
