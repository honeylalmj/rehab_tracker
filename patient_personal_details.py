from kivy.lang import Builder
from kivymd.app import MDApp
from patient_verification import PatientVerification
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu
import random
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from send_email import send_email
import json
import os
import sys

KV = '''
FloatLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1.0  # White background color (RGBA values)
        Rectangle:
            pos: self.pos
            size: self.size
    MDLabel:
        text: "Patient details"
        theme_text_color: "Custom"
        text_color: "blue"
        pos_hint: {"center_x": 0.6,"center_y": 0.9}
        size_hint: 0.3, 0.1        
    MDTextField:
        id: text_field_patientname
        hint_text: "First name"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.35,"center_y": 0.8}
        size_hint: 0.25, 0.1
    MDTextField:
        id: text_field_patientlastname
        hint_text: "Last name"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.62,"center_y": 0.8}
        size_hint: 0.25, 0.1
    MDLabel:
        text: "Sex :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.65, "center_y": 0.7}
        size_hint: 0.3, 0.1
    MDTextField:
        id: text_field_age
        hint_text: "Age"
        multiline: True
        mode: "rectangle"
        pos_hint: {"center_x": 0.35,"center_y": 0.7}
        size_hint: 0.25, 0.1
    IconListItem:
        id: drop_item
        pos_hint: {'center_x': 0.65, 'center_y': 0.7}
        text: 'select'
        text_color: "black"
        size_hint: 0.18, 0.04
        on_release: app.menu.open()    
    MDTextField:
        id: text_field_housename
        hint_text: "House name "
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.35, "center_y": 0.6}
        size_hint: 0.25, 0.1
    MDTextField:
        id: text_field_streetname
        hint_text: "Street name"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.62, "center_y": 0.6}
        size_hint: 0.25, 0.1
    MDTextField:
        id: text_field_city
        hint_text: "City"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.35, "center_y": 0.5}
        size_hint: 0.25, 0.1
    MDTextField:
        id: text_field_postalcode
        hint_text: "Postal code"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.62, "center_y": 0.5}
        size_hint: 0.25, 0.1
    MDTextField:
        id: text_field_patientemail
        hint_text: "Email id"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.485, "center_y": 0.4}
        size_hint: 0.52, 0.1
    MDTextField:
        id: text_field_patientmobilenumber
        hint_text: "Mobile number"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.485, "center_y": 0.3}
        size_hint: 0.52, 0.1
    MDRaisedButton:
        text: "Next"
        md_bg_color: "green"
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        size_hint: 0.1, 0.08
        on_press: app.next()
'''
class IconListItem(OneLineIconListItem):
    icon = StringProperty()
class PatientPersonalDetails(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if getattr(sys, 'frozen', False):
            # Running as a PyInstaller executable
            base_path = sys._MEIPASS
        else:
            # Running as a script
            base_path = os.path.abspath(".")
        
        self.patient_json_file_path = os.path.join(base_path,'patient_data.json')
        self.screen = Builder.load_string(KV)
        self.verification_code = random.randint(100000,999999)
        self.patient_id = random.randint(1000,9999)
        self.patient_detail = {}
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
            },
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": f"Others",
                "height": dp(56),
                "on_release": lambda x="Others": self.set_item(x),
            }
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=4,
        )

    def save_file(self):
        try:
            with open(self.patient_json_file_path, 'r') as file:
                existing_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = {}

        existing_data.update(self.patient_detail)

        with open(self.patient_json_file_path, 'w') as file:
            json.dump(existing_data, file, indent=2)
        file.close()


    def read_file(self):
        try:
            with open(self.patient_json_file_path,'r')as file :
                data = json.load(file)
                return data
        except(FileNotFoundError, json.JSONDecodeError,KeyError):
            return{}
        
    def set_item(self, text_item):
        self.screen.ids.drop_item.text = text_item
        self.menu.dismiss()   

    def build(self):
      
        self.screen.ids.text_field_patientname.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        self.screen.ids.text_field_patientlastname.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        self.screen.ids.drop_item.bind(
            on_text=self.set_error_message,
        )
        self.screen.ids.text_field_age.bind(
            on_text=self.set_error_message,
        )
        self.screen.ids.text_field_housename.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        self.screen.ids.text_field_streetname.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        self.screen.ids.text_field_city.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        self.screen.ids.text_field_postalcode.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        self.screen.ids.text_field_patientemail.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        self.screen.ids.text_field_patientmobilenumber.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )

        return self.screen

    def set_error_message(self, instance_textfield, value=None):
        if not instance_textfield.text.strip() or (instance_textfield == self.screen.ids.drop_item and (value is None or value == "select")):
            instance_textfield.error = True
            instance_textfield.helper_text = "Required field"
        else:
            instance_textfield.error = False
            instance_textfield.helper_text = ""

    def show_verification_Dialog(self):
        dialog = MDDialog(
            text="Verification code with Patient ID sent successfully !",
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: self.handle_verification_success_dialog_dismiss(dialog)
                )
            ]
        )
        dialog.open()
    
    def handle_verification_success_dialog_dismiss(self,dialog):
        dialog.dismiss()
        self.stop() 
        PatientVerification(self.verification_code,self.patient_id).run()
    def next(self):
    
        patient_name = self.screen.ids.text_field_patientname.text.strip()
        patient_last_name = self.screen.ids.text_field_patientlastname.text.strip()
        age = self.screen.ids.text_field_age.text
        sex = self.screen.ids.drop_item.text
        house_name = self.screen.ids.text_field_housename.text.strip()
        street_name = self.screen.ids.text_field_streetname.text.strip()
        city = self.screen.ids.text_field_city.text.strip()
        postal_code = self.screen.ids.text_field_postalcode.text.strip()
        patient_email = self.screen.ids.text_field_patientemail.text.strip()
        patient_mobile_number = self.screen.ids.text_field_patientmobilenumber.text.strip()

        self.screen.ids.text_field_patientname.error = False
        self.screen.ids.text_field_patientlastname.error = False
        self.screen.ids.text_field_age.error = False
        self.screen.ids.drop_item.error = False
        self.screen.ids.text_field_housename.error = False
        self.screen.ids.text_field_streetname.error = False
        self.screen.ids.text_field_city.error = False
        self.screen.ids.text_field_postalcode.error = False
        self.screen.ids.text_field_patientemail.error = False
        self.screen.ids.text_field_patientmobilenumber.error = False

        if not patient_name:
            self.screen.ids.text_field_patientname.error = True
            self.screen.ids.text_field_patientname.helper_text = "Required field"

        if not patient_last_name:
            self.screen.ids.text_field_patientlastname.error = True
            self.screen.ids.text_field_patientlastname.helper_text = "Required field"
        if not age:
            self.screen.ids.text_field_age.error = True
            self.screen.ids.text_field_age.helper_text = "Required field"

        if not sex:
            self.screen.ids.drop_item.error = True
            self.screen.ids.drop_item.helper_text = "Required field"   

        if not house_name:
            self.screen.ids.text_field_housename.error = True
            self.screen.ids.text_field_housename.helper_text = "Required field"

        if not street_name:
            self.screen.ids.text_field_streetname.error = True
            self.screen.ids.text_field_streetname.helper_text = "Required field"

        if not city:
            self.screen.ids.text_field_city.error = True
            self.screen.ids.text_field_city.helper_text = "Required field"

        if not postal_code:
            self.screen.ids.text_field_postalcode.error = True
            self.screen.ids.text_field_postalcode.helper_text = "Required field"

        if not patient_email:
            self.screen.ids.text_field_patientemail.error = True
            self.screen.ids.text_field_patientemail.helper_text = "Required field"

        if not patient_mobile_number:
            self.screen.ids.text_field_patientmobilenumber.error = True
            self.screen.ids.text_field_patientmobilenumber.helper_text = "Required field"            

        existing_data = self.read_file()
        if (age
            and (sex != "select")
            and patient_name 
            and patient_last_name 
            and house_name 
            and street_name 
            and city and 
            postal_code 
            and patient_email 
            and patient_mobile_number) :
            patient_data = {'Personal details ' :{"Patient Name": patient_name,
                            "Patient Last Name": patient_last_name,
                            "Age": age,
                            "Sex": sex,
                            "House Name": house_name,
                            "Street Name": street_name,
                            "City": city,
                            "Postal Code": postal_code,
                            "Patient Email": patient_email,
                            "Patient Mobile Number": patient_mobile_number}}
            
            send_email(patient_name,self.verification_code,self.patient_id,patient_email)
            if self.patient_id not in existing_data:
                self.patient_detail[self.patient_id] = patient_data
                print(self.patient_detail)
            

                self.save_file()
                self.show_verification_Dialog()
            else:
              print("Fields are missing or incorrect.")

           

if __name__ == "__main__":
    PatientPersonalDetails().run()
