from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.icon_definitions import md_icons
import json

KV = '''
FloatLayout:
    canvas.before:
        Color:
            rgba: 0.784, 0.784, 0.941, 1.0  # Lavender background color (RGBA values)
        Rectangle:
            pos: self.pos
            size: self.size
    MDLabel:
        text: "Rehab Tracker"
        theme_text_color: "Custom"
        text_color: "blue"
        pos_hint: {"center_x": 0.6,"center_y": 0.8}
        size_hint: 0.3,0.1

    MDTextField:
        id: text_field_error
        hint_text: "Username"
        mode: "rectangle"
        pos_hint: {"center_x": 0.5,"center_y": 0.7}
        size_hint: 0.5,0.1

    MDTextField:
        id: text_field_error1
        hint_text: "Password"
        mode: "rectangle"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint:0.5,0.1

    MDRaisedButton:
        text: "login"
        md_bg_color: "green"
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        size_hint:0.1, 0.08
        on_press : app.login()

    MDTextButton:
        text: "Forget Password ?"
        custom_color: "black"  
        pos_hint: {"center_x": 0.6, "center_y": 0.35}
        size_hint:0.3,0.1  
    MDRoundFlatButton:
        text: "Create new account"
        text_color: "black"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint:0.3,0.1
               
'''

class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        self.dialog = None  # Initialize dialog instance

    def build(self):
        return self.screen

    def read_data(self):
        try:
            with open("username.json", "r") as file:
                user_name = json.load(file)
            return user_name
        except (FileNotFoundError, KeyError):
            print("username not found in json")
            return {}

    def create_dialog(self, text):
        if self.dialog:
            self.dialog.text = text  # Update dialog text
        else:
            self.dialog = MDDialog(
                text=text,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()

    def login(self):
        username = self.screen.ids.text_field_error.text.strip()
        password = self.screen.ids.text_field_error1.text.strip()
        user_data = self.read_data()
        if username and password:
            if user_data and username in user_data and password in user_data[username]:
                print(username)
                print(password)
            else:
                self.create_dialog("Username or password error")
        else:
            print("Please enter username and password")
            self.create_dialog("Please enter correct username and password")

if __name__ == "__main__":
    Test().run()
