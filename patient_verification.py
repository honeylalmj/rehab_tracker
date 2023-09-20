from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
FloatLayout:
    canvas.before:
        Color:
            rgba: 0.784, 0.784, 0.941, 1.0  # Lavender background color (RGBA values)
        Rectangle:
            pos: self.pos
            size: self.size
    MDTextField:
        id: text_field_verification
        hint_text: "Verification code"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.5, "center_y": 0.65}
        size_hint: 0.55, 0.1
    MDRaisedButton:
        text: "Next"
        md_bg_color: "green"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint: 0.1, 0.08
        on_press: app.next()
'''

class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
       
        self.screen.ids.text_field_verification.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        
        return self.screen

    def set_error_message(self):
       pass

    def next(self):
        # Implement your registration logic here
        pass

if __name__ == "__main__":
    Test().run()
