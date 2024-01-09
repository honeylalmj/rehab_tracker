from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.properties import StringProperty
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
        text: "Treatment Plan"
        theme_text_color: "Custom"
        text_color: "blue"
        pos_hint: {"center_x": 0.6,"center_y": 0.9}
        size_hint: 0.3, 0.1
    MDLabel:
        text: "Treatment plan :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.75, "center_y": 0.8}
   
    MDTextField:
        id: shortplan_textfield
        hint_text: "Short term goal"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint: 0.5, 0.1
         
    MDTextField:
        id: longplan_textfield
        hint_text: "Long term goal"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: 0.5, 0.1
    MDLabel:
        text: "Treatment :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.75, "center_y": 0.49}    
    MDTextField:
        id: treatment_textfield
        hint_text: ""
        multiline: True
        pos_hint: {"center_x": 0.55, "center_y": 0.5}
        size_hint: 0.4, 0.1
    IconListItem:
        id: drop_item
        pos_hint: {'center_x': 0.45, 'center_y': 0.4}
        text: 'select'
        text_color: "black"
        size_hint: 0.18, 0.04
        on_release: app.menu.open()    
    MDLabel:
        text: "Prognosis :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.75, "center_y": 0.4}    
   
    MDRaisedButton:
        text: "Finish"
        md_bg_color: "green"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint: 0.1, 0.08
        on_press: app.next()
             
'''
class IconListItem(OneLineIconListItem):
    icon = StringProperty()


class PatientTreatment(MDApp):
    def __init__(self,patient_no,date, **kwargs):
        super().__init__(**kwargs)
        if getattr(sys, 'frozen', False):
            # Running as a PyInstaller executable
            base_path = sys._MEIPASS
        else:
            # Running as a script
            base_path = os.path.abspath(".")
        # script_dir = os.path.dirname(os.path.abspath(__file__))
        self.patient_json_file_path = os.path.join(base_path,'patient_data.json')
        self.screen = Builder.load_string(KV)
        self.patient = patient_no
        self.date = date
        self.data = {}

        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": f"Good",
                "height": dp(56),
                "on_release": lambda x="Good": self.set_item(x),
            },
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": f"Bad",
                "height": dp(56),
                "on_release": lambda x="Bad": self.set_item(x),
            }
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=4,
        )  
    

    def set_item(self, text_item):
        self.screen.ids.drop_item.text = text_item
        self.menu.dismiss()     

    def build(self):
        self.screen.ids.shortplan_textfield.bind(
            on_text=self.set_error_message,
        )
        self.screen.ids.longplan_textfield.bind(
            on_text=self.set_error_message,
        )
        self.screen.ids.treatment_textfield.bind(
            on_text=self.set_error_message, 
        )
        self.screen.ids.drop_item.bind(
            on_text=self.set_error_message,
        )
        return self.screen
    
    def save_file(self):
        try:
            with open(self.patient_json_file_path,'r')as file:
                existing_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = {}
        patient_id = str(self.patient)

        if patient_id in existing_data:
            existing_data[patient_id][self.date].update(self.data)  
        with open(self.patient_json_file_path,'w') as file :
            json.dump(existing_data,file, indent=2)
        file.close()  

    def set_error_message(self, instance_textfield, value):
        if not instance_textfield.text.strip() or (instance_textfield == self.screen.ids.drop_item and value == "select"):
            instance_textfield.error = True
            instance_textfield.helper_text = "Required field"
        else:
            instance_textfield.error = False
            instance_textfield.helper_text = ""
    def show_verification_Dialog(self):
        dialog = MDDialog(
            text="All patient data entered has been saved successfully !",
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
        from home_page import HomePage
        HomePage().run()

    def next(self):
       
        short_term_plan = self.screen.ids.shortplan_textfield.text
        long_term_plan = self.screen.ids.longplan_textfield.text
        treatment = self.screen.ids.treatment_textfield.text
        prognosis = self.screen.ids.drop_item.text
       
       
        self.screen.ids.shortplan_textfield.error = False
        self.screen.ids.longplan_textfield.error = False
        self.screen.ids.treatment_textfield.error = False
        self.screen.ids.drop_item.error = False

     

        if not short_term_plan:
            self.screen.ids.shortplan_textfield.error = True
            self.screen.ids.shortplan_textfield.helper_text = "Required field"

        if not long_term_plan:
            self.screen.ids.longplan_textfield.error = True
            self.screen.ids.longplan_textfield.helper_text = "Required field"

        if not treatment:
            self.screen.ids.treatment_textfield.error = True
            self.screen.ids.treatment_textfield.helper_text = "Required field"

        if not prognosis:
            self.screen.ids.drop_item.error = True
            self.screen.ids.drop_item.helper_text = "Required field"
        
        if (
            short_term_plan
            and long_term_plan
            and treatment
            and (prognosis != "select")
        ):
            
            treatment_plan = {"Short term goal": short_term_plan,
                            "Long term goal": long_term_plan}
            
            self.data['Treatment plan'] = treatment_plan
            self.data['Treatment'] = {'Treatment':treatment}
            self.data['Prognosis'] = {'Prognosis' :prognosis}
            self.save_file()
            print(self.data)
            self.show_verification_Dialog()


            
            
            
if __name__ == "__main__":
    PatientTreatment().run()
    
