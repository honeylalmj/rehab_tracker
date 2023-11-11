from kivy.lang import Builder
from kivymd.app import MDApp
from patient_verification import PatientVerification
import random
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from send_email import send_email

KV = '''
FloatLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1.0  # White background color (RGBA values)
        Rectangle:
            pos: self.pos
            size: self.size
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
    MDTextField:
        id: text_field_housename
        hint_text: "House name "
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.35, "center_y": 0.7}
        size_hint: 0.25, 0.1
    MDTextField:
        id: text_field_streetname
        hint_text: "Street name"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.62, "center_y": 0.7}
        size_hint: 0.25, 0.1
    MDTextField:
        id: text_field_city
        hint_text: "City"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.35, "center_y": 0.6}
        size_hint: 0.25, 0.1
    MDTextField:
        id: text_field_postalcode
        hint_text: "Postal code"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.62, "center_y": 0.6}
        size_hint: 0.25, 0.1
    MDTextField:
        id: text_field_patientemail
        hint_text: "Email id"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.485, "center_y": 0.5}
        size_hint: 0.52, 0.1
    MDTextField:
        id: text_field_patientmobilenumber
        hint_text: "Mobile number"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        mode: "rectangle"
        pos_hint: {"center_x": 0.485, "center_y": 0.4}
        size_hint: 0.52, 0.1
    MDRaisedButton:
        text: "Next"
        md_bg_color: "green"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint: 0.1, 0.08
        on_press: app.next()
'''

class PatientPersonalDetails(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        self.verification_code = random.randint(100000,999999)
        self.patient_id = random.randint(1000,9999)

    def build(self):
        # Bind validation and error handling for text fields
        self.screen.ids.text_field_patientname.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        self.screen.ids.text_field_patientlastname.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
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

    def set_error_message(self, instance_textfield):
        # This function should handle error messages if needed
        # For example, check if the field is empty and set an error message

        if not instance_textfield.text.strip():
            instance_textfield.error = True
            instance_textfield.helper_text = "Required field"
        else:
            instance_textfield.error = False
            instance_textfield.helper_text = ""
    def show_verification_Dialog(self):
        dialog = MDDialog(
            text="Verification code with Patient ID sent successfully",
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
    # Implement your logic for the "Next" button here
    # You can access the text from the text fields using self.screen.ids
        patient_name = self.screen.ids.text_field_patientname.text.strip()
        patient_last_name = self.screen.ids.text_field_patientlastname.text.strip()
        house_name = self.screen.ids.text_field_housename.text.strip()
        street_name = self.screen.ids.text_field_streetname.text.strip()
        city = self.screen.ids.text_field_city.text.strip()
        postal_code = self.screen.ids.text_field_postalcode.text.strip()
        patient_email = self.screen.ids.text_field_patientemail.text.strip()
        patient_mobile_number = self.screen.ids.text_field_patientmobilenumber.text.strip()

    # Clear error flags and helper text
        self.screen.ids.text_field_patientname.error = False
        self.screen.ids.text_field_patientlastname.error = False
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

        # Implement your logic to process the input data here
        # For example, you can print the input data
        if patient_name and patient_last_name and house_name and street_name and city and postal_code and patient_email and patient_mobile_number :
            print(f"Patient Name: {patient_name}")
            print(f"Patient Last Name: {patient_last_name}")
            print(f"House Name: {house_name}")
            print(f"Street Name: {street_name}")
            print(f"City: {city}")
            print(f"Postal Code: {postal_code}")
            print(f"Patient Email: {patient_email}")
            print(f"Patient Mobile Number: {patient_mobile_number}")
            send_email(patient_name,self.verification_code,self.patient_id,patient_email)
            self.show_verification_Dialog()
            

           

if __name__ == "__main__":
    PatientPersonalDetails().run()
