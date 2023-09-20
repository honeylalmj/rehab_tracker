from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker

KV = '''
FloatLayout:
    canvas.before:
        Color:
            rgba: 0.784, 0.784, 0.941, 1.0  # Lavender background color (RGBA values)
        Rectangle:
            pos: self.pos
            size: self.size
    MDLabel:
        text: "Date :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.4, "center_y": 0.9}
        size_hint: 0.3, 0.1
    MDRaisedButton:
        id: date_button
        text: "Select Date"
        pos_hint: {'center_x': 0.38, 'center_y': 0.9}
        size_hint: 0.01, 0.01
        on_release: app.show_date_picker()
    MDLabel:
        text: "Sex :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.65, "center_y": 0.9}
        size_hint: 0.3, 0.1
    MDLabel:
        text: "Age :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.4, "center_y": 0.8}
        size_hint: 0.3, 0.1
    MDTextField:
        id: text_field_age
        multiline: True
        pos_hint: {"center_x": 0.35, "center_y": 0.8}
        size_hint: 0.1, 0.1
    IconListItem:
        id: drop_item
        pos_hint: {'center_x': 0.65, 'center_y': 0.9}
        text: 'select'
        text_color: "black"
        size_hint: 0.18, 0.04
        on_release: app.menu.open()
    MDLabel:
        text: "Patient Medical History :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.75, "center_y": 0.7}

    MDTextField:
        id: past_textfield
        hint_text: "Enter Past Medical History"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: 0.5, 0.1
         
    MDTextField:
        id: present_textfield
        hint_text: "Enter Present Medical History"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: 0.5, 0.1
    MDLabel:
        text: "Physical examination :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.75, "center_y": 0.4}    
    MDTextField:
        id: textfield_physical
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        size_hint: 0.5, 0.1
    MDRaisedButton:
        text: "Next"
        md_bg_color: "green"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint: 0.1, 0.08
        on_press: app.next()
             
'''

class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": f"Male",
                "height": dp(56),
                "on_release": lambda x="Male": self.set_item(x),
            },
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": f"Female",
                "height": dp(56),
                "on_release": lambda x="Female": self.set_item(x),
            }
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=4,
        )

    def on_save(self, instance, value, date_range):
        print(instance, value, date_range)
        self.screen.ids.date_button.text = f' {value.strftime("%d-%m-%Y")}'

    def on_cancel(self, instance, value):
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def set_item(self, text_item):
        self.screen.ids.drop_item.text = text_item
        self.menu.dismiss()     

    def build(self):
        self.screen.ids.text_field_age.bind(
            on_text=self.set_error_message,
        )
        self.screen.ids.past_textfield.bind(
            on_text=self.set_error_message,
        )
        self.screen.ids.present_textfield.bind(
            on_text=self.set_error_message, 
        )
        self.screen.ids.textfield_physical.bind(
            on_text=self.set_error_message, 
        )
        
        return self.screen

    def set_error_message(self, instance_textfield, value):
        if not instance_textfield.text.strip():
            instance_textfield.error = True
            instance_textfield.helper_text = "Required field"
        else:
            instance_textfield.error = False
            instance_textfield.helper_text = ""

    def next(self):
        # Check if any of the required fields are empty
        age = self.screen.ids.text_field_age.text.strip()
        sex = self.screen.ids.drop_item.text.strip()
        past_medical_history = self.screen.ids.past_textfield.text.strip()
        present_medical_history = self.screen.ids.present_textfield.text.strip()
        physical_examination = self.screen.ids.textfield_physical.text.strip()
        selected_date = self.screen.ids.date_button.text.strip()

        # Reset error messages for all fields
        self.screen.ids.text_field_age.error = False
        self.screen.ids.drop_item.error = False
        self.screen.ids.past_textfield.error = False
        self.screen.ids.present_textfield.error = False
        self.screen.ids.textfield_physical.error = False
        self.screen.ids.date_button.error = False

        if not age:
            self.screen.ids.text_field_age.error = True
            self.screen.ids.text_field_age.helper_text = "Required field"

        if not sex:
            self.screen.ids.drop_item.error = True

        if not past_medical_history:
            self.screen.ids.past_textfield.error = True
            self.screen.ids.past_textfield.helper_text = "Required field"

        if not present_medical_history:
            self.screen.ids.present_textfield.error = True
            self.screen.ids.present_textfield.helper_text = "Required field"

        if not physical_examination:
            self.screen.ids.textfield_physical.error = True
            self.screen.ids.textfield_physical.helper_text = "Required field"

        if not selected_date or selected_date == "Select Date":
            self.screen.ids.date_button.error = True

        if (
            age
            and sex
            and past_medical_history
            and present_medical_history
            and physical_examination
            and selected_date
        ):
            # Implement your logic to process the input data here
            # For example, you can print the input data
            print(f"Age: {age}")
            print(f"Sex: {sex}")
            print(f"Past Medical History: {past_medical_history}")
            print(f"Present Medical History: {present_medical_history}")
            print(f"Physical Examination: {physical_examination}")
            print(f"Selected Date: {selected_date}")

if __name__ == "__main__":
    Test().run()
