from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from view_patient import ViewPatientScreen
import json
import os
import sys
KV = '''
BoxLayout:
    orientation: 'vertical'
    ScrollView:
        MDBoxLayout:
            id: container
            orientation: 'vertical'
    MDRaisedButton:
        text: 'Back'
        on_press: app.back()
'''

class DisplayPatientDataApp(MDApp):
    def __init__(self, patient_id, consultation_date, **kwargs):
        super().__init__(**kwargs)
        if getattr(sys, 'frozen', False):
            base_path = os.path.dirname(sys.executable)
        else:
            base_path = os.path.dirname(__file__)
        self.patient_json_file_path = os.path.join(base_path,'patient_data.json')
        self.patient_id = patient_id
        self.consultation_date = consultation_date
        self.data = self.read_file()

    def read_file(self):
        try:
            with open(self.patient_json_file_path, 'r') as file:
                patient_data = json.load(file)
                return patient_data
        except (FileNotFoundError, KeyError, json.JSONDecodeError):
            print("Data not found")
            return {}

    def build(self):
        self.root = Builder.load_string(KV)
        self.display_data()
        return self.root

    def back(self):
        # Clear current widgets
        self.root.ids.container.clear_widgets()
        from view_patient import ViewPatientScreen
        ViewPatientScreen().run()

    def display_data(self):
        self.root.ids.container.clear_widgets()

        if self.patient_id is not None and self.consultation_date is not None:
            patient_details = self.data.get(self.patient_id, {}).get("Personal details ", {})
            consultation_details = self.data.get(self.patient_id, {}).get(self.consultation_date, {})

            if patient_details:
                self.add_rich_label("Personal details", patient_details)
            else:
                self.add_label("No data available")

            if consultation_details:
                for category, details in consultation_details.items():
                    self.add_rich_label(category, details)
            else:
                self.add_label("No data available")

        else:
            self.add_label("Patient ID and consultation date not provided")

    def add_label(self, text):
        label = MDLabel(text=text, theme_text_color="Primary", font_style='Body1')
        self.root.ids.container.add_widget(label)

    def add_rich_label(self, category, details):
        rich_label = MDLabel(
            text=f"[b]{category}[/b]: {details}",
            theme_text_color="Primary",
            markup=True
        )
        self.root.ids.container.add_widget(rich_label)


if __name__ == '__main__':
    DisplayPatientDataApp().run()
