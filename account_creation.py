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

    MDLabel:
        text: "Hi, Physio..."
        theme_text_color: "Custom"
        text_color: "blue"
        pos_hint: {"center_x": 0.6,"center_y": 0.9}
        size_hint: 0.3, 0.1

    MDTextField:
        id: text_field_firstname
        hint_text: "First name"
        mode: "rectangle"
        pos_hint: {"center_x": 0.35,"center_y": 0.8}
        size_hint: 0.25, 0.1

    MDTextField:
        id: text_field_lastname
        hint_text: "Last name"
        mode: "rectangle"
        pos_hint: {"center_x": 0.65,"center_y": 0.8}
        size_hint: 0.25, 0.1

    MDTextField:
        id: text_field_licensenumber
        hint_text: "License number"
        mode: "rectangle"
        pos_hint: {"center_x": 0.5, "center_y": 0.65}
        size_hint: 0.55, 0.1

    MDTextField:
        id: text_field_mobilenumber
        hint_text: "Mobile number"
        mode: "rectangle"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: 0.55, 0.1

    MDTextField:
        id: text_field_email
        hint_text: "Email id"
        mode: "rectangle"
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        size_hint: 0.55, 0.1

    MDRaisedButton:
        text: "Register"
        md_bg_color: "green"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint: 0.1, 0.08
        on_press: app.register()
'''

class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        # Bind validation and error handling for text fields
        self.screen.ids.text_field_firstname.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        self.screen.ids.text_field_lastname.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        self.screen.ids.text_field_licensenumber.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        self.screen.ids.text_field_mobilenumber.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        self.screen.ids.text_field_email.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )

        return self.screen

    def set_error_message(self, instance_textfield):
        # This function should handle error messages if needed
        # For example, check if the field is empty and set an error message

        if not instance_textfield.text.strip():
            instance_textfield.error = True
            instance_textfield.helper_text = "Required field"
        else:
            instance_textfield.error = False
            instance_textfield.helper_text = ""

    def register(self):
        first_name = self.screen.ids.text_field_firstname.text.strip()
        last_name = self.screen.ids.text_field_lastname.text.strip()
        license_number = self.screen.ids.text_field_licensenumber.text.strip()
        mobile_number = self.screen.ids.text_field_mobilenumber.text.strip()
        email = self.screen.ids.text_field_email.text.strip()

        # Reset error messages for all fields
        self.screen.ids.text_field_firstname.error = False
        self.screen.ids.text_field_lastname.error = False
        self.screen.ids.text_field_licensenumber.error = False
        self.screen.ids.text_field_mobilenumber.error = False
        self.screen.ids.text_field_email.error = False

        if not first_name:
            self.screen.ids.text_field_firstname.error = True
            self.screen.ids.text_field_firstname.helper_text = "Required field"

        if not last_name:
            self.screen.ids.text_field_lastname.error = True
            self.screen.ids.text_field_lastname.helper_text = "Required field"

        if not license_number:
            self.screen.ids.text_field_licensenumber.error = True
            self.screen.ids.text_field_licensenumber.helper_text = "Required field"

        if not mobile_number:
            self.screen.ids.text_field_mobilenumber.error = True
            self.screen.ids.text_field_mobilenumber.helper_text = "Required field"

        if not email:
            self.screen.ids.text_field_email.error = True
            self.screen.ids.text_field_email.helper_text = "Required field"

        if first_name and last_name and license_number and mobile_number and email:
            # Implement your registration logic here
            # For example, you can print the input data
            print(f"Registered: {first_name}, {last_name}, {license_number}, {mobile_number}, {email}")

if __name__ == "__main__":
    Test().run()
