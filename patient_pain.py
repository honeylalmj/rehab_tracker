from kivy.lang import Builder
from kivymd.app import MDApp
from patient_range import PatientRange
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
        text: "Patient Assessment"
        theme_text_color: "Custom"
        text_color: "blue"
        pos_hint: {"center_x": 0.6,"center_y": 0.9}
        size_hint: 0.3, 0.1
    MDLabel:
        text: "Range of motion : Upper limb"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.58, "center_y": 0.8}
        size_hint: 0.3, 0.1
    MDLabel:
        text: "Shoulder :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.45, "center_y": 0.7}
        size_hint: 0.3, 0.1
    MDTextField:
        id: shoulder_active_textfield_l
        hint_text: "Active range (L)"
        multiline: True
        pos_hint: {"center_x": 0.4, "center_y": 0.7}
        size_hint: 0.05, 0.08
    MDTextField:
        id: shoulder_active_textfield_r
        hint_text: "Active range (R)"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint: 0.05, 0.08    
    MDTextField:
        id: shoulder_passive_textfield_l
        hint_text: "Passive range (L)"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.7}
        size_hint: 0.05, 0.08
    MDTextField:
        id: shoulder_passive_textfield_r
        hint_text: "Passive range (R)"
        multiline: True
        pos_hint: {"center_x": 0.7, "center_y": 0.7}
        size_hint: 0.05, 0.08    
    MDLabel:
        text: "Elbow :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.45, "center_y": 0.6}
        size_hint: 0.3, 0.1
    MDTextField:
        id: elbow_active_textfield_l
        hint_text: "Active range (L)"
        multiline: True
        pos_hint: {"center_x": 0.4, "center_y": 0.6}
        size_hint: 0.05, 0.08
    MDTextField:
        id: elbow_active_textfield_r
        hint_text: "Passive range (R)"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: 0.05, 0.08
    MDTextField:
        id: elbow_passive_textfield_l
        hint_text: "Active range (L)"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.6}
        size_hint: 0.05, 0.08
    MDTextField:
        id: elbow_passive_textfield_r
        hint_text: "Passive range (R)"
        multiline: True
        pos_hint: {"center_x": 0.7, "center_y": 0.6}
        size_hint: 0.05, 0.08    
    MDLabel:
        text: "Forearm :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.45, "center_y": 0.5}
        size_hint: 0.3, 0.1
    MDTextField:
        id: forearm_active_textfield_l
        hint_text: "Active range (L)"
        multiline: True
        pos_hint: {"center_x": 0.4, "center_y": 0.5}
        size_hint: 0.05, 0.08
    MDTextField:
        id: forearm_active_textfield_r
        hint_text: "Active range (R)"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: 0.05, 0.08    
    MDTextField:
        id: forearm_passive_textfield_l
        hint_text: "Passive range (L)"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.5}
        size_hint: 0.05, 0.08
    MDTextField:
        id: forearm_passive_textfield_r
        hint_text: "Passive range (R)"
        multiline: True
        pos_hint: {"center_x": 0.7, "center_y": 0.5}
        size_hint: 0.05, 0.08    
    MDLabel:
        text: "Wrist :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.45, "center_y": 0.4}
        size_hint: 0.3, 0.1
    MDTextField:
        id: wrist_active_textfield_l
        hint_text: "Active range (L)"
        multiline: True
        pos_hint: {"center_x": 0.4, "center_y": 0.4}
        size_hint: 0.05, 0.08
    MDTextField:
        id: wrist_active_textfield_r
        hint_text: "Active range (R)"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        size_hint: 0.05, 0.08    
    MDTextField:
        id: wrist_passive_textfield_l
        hint_text: "Passive range (L)"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.4}
        size_hint: 0.05, 0.08
    MDTextField:
        id: wrist_passive_textfield_r
        hint_text: "Passive range (R)"
        multiline: True
        pos_hint: {"center_x": 0.7, "center_y": 0.4}
        size_hint: 0.05, 0.08    
    MDLabel:
        text: "Fingers :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.45, "center_y": 0.3}
        size_hint: 0.3, 0.1
    MDTextField:
        id: finger_active_textfield_l
        hint_text: "Active range (L)"
        multiline: True
        pos_hint: {"center_x": 0.4, "center_y": 0.3}
        size_hint: 0.05, 0.08
    MDTextField:
        id: finger_active_textfield_r
        hint_text: "Active range (R)"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        size_hint: 0.05, 0.08    
    MDTextField:
        id: finger_passive_textfield_l
        hint_text: "Passive range (L)"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.3}
        size_hint: 0.05, 0.08 
    MDTextField:
        id: finger_passive_textfield_r
        hint_text: "Passive range (R)"
        multiline: True
        pos_hint: {"center_x": 0.7, "center_y": 0.3}
        size_hint: 0.05, 0.08     
    MDRaisedButton:
        text: "Next"
        md_bg_color: "green"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint: 0.1, 0.08
        on_press: app.next()                  
'''

class PatientPain(MDApp):
    def __init__(self,patient_no,date,**kwargs):
        super().__init__(**kwargs)
        if getattr(sys, 'frozen', False):
            # Running as a PyInstaller executable
            base_path = sys._MEIPASS
        else:
            # Running as a script
            base_path = os.path.abspath(".")
        # script_dir = os.path.dirname(os.path.abspath(__file__))
        self.patient_json_file_path = os.path.join(base_path,'patient_data.json')
        self.patient = patient_no
        self.date = date
        self.data = {}
        
  
    
    limb_textfield_ids = {
            "Shoulder": ("shoulder_active_textfield_l","shoulder_active_textfield_r","shoulder_passive_textfield_l","shoulder_passive_textfield_r"),
            "Elbow": ("elbow_active_textfield_l","elbow_active_textfield_r","elbow_passive_textfield_l", "elbow_passive_textfield_r"),
            "Forearm": ("forearm_active_textfield_l","forearm_active_textfield_r", "forearm_passive_textfield_l","forearm_passive_textfield_r"),
            "Wrist": ("wrist_active_textfield_l","wrist_active_textfield_r","wrist_passive_textfield_l","wrist_passive_textfield_r"),
            "Fingers": ("finger_active_textfield_l","finger_active_textfield_r", "finger_passive_textfield_l","finger_passive_textfield_r"),
        }
    
    def build(self):
        return Builder.load_string(KV)
    
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
        if not instance_textfield.text.strip():
            instance_textfield.error = True
            instance_textfield.helper_text = "Required field"
        else:
            instance_textfield.error = False
            instance_textfield.helper_text = ""

    def nextpage(self):
        self.stop()
        PatientRange(self.patient,self.date).run()  

    def next(self):

        
        for limb, (active_left_id,active_right_id, passive_left_id,passive_right_id) in self.limb_textfield_ids.items():
            active_left_range = self.root.ids[active_left_id].text.strip()
            active_right_range = self.root.ids[active_right_id].text.strip()
            passive_left_range = self.root.ids[passive_left_id].text.strip()
            passive_right_range = self.root.ids[passive_right_id].text.strip()

            if not active_left_range:
                self.root.ids[active_left_id].error = True
                self.root.ids[active_left_id].helper_text = "Required field"
            else:
                self.root.ids[active_left_id].error = False
                self.root.ids[active_left_id].helper_text = ""

            if not active_right_range:
                self.root.ids[active_right_id].error = True
                self.root.ids[active_right_id].helper_text = "Required field"
            else:
                self.root.ids[active_right_id].error = False
                self.root.ids[active_right_id].helper_text = ""
    
            if not passive_left_range:
                self.root.ids[passive_left_id].error = True
                self.root.ids[passive_left_id].helper_text = "Required field"
            else:
                self.root.ids[passive_left_id].error = False
                self.root.ids[passive_left_id].helper_text = ""

            if not passive_right_range:
                self.root.ids[passive_right_id].error = True
                self.root.ids[passive_right_id].helper_text = "Required field"
            else:
                self.root.ids[passive_right_id].error = False
                self.root.ids[passive_right_id].helper_text = ""
        if (
           
             all(
                not self.root.ids[active_left_id].error and not self.root.ids[active_right_id].error and not self.root.ids[passive_left_id].error and not self.root.ids[passive_right_id].error
                for active_left_id,active_right_id,passive_left_id,passive_right_id in self.limb_textfield_ids.values()
            )
        ):        
             

            limb_assessments = {}   

            for limb, (active_left_id,active_right_id,passive_left_id, passive_right_id) in self.limb_textfield_ids.items():
                active_left_range = self.root.ids[active_left_id].text.strip()
                active_right_range = self.root.ids[active_right_id].text.strip()
                passive_left_range = self.root.ids[passive_left_id].text.strip()
                passive_right_range = self.root.ids[passive_right_id].text.strip()

                pain_assessment = {"Active Range (L)": active_left_range,
                                   "Active Range (R)" : active_right_range,
                                   "Passive Range (L)" : passive_left_range,
                                    "Passive Range (R)": passive_right_range }
                limb_assessments[limb] = pain_assessment 
            
            self.data['Range of motion for Upper limb']= limb_assessments

            self.save_file()    
            print(self.data)   
            self.nextpage() 
            
                  

if __name__ == '__main__':
    PatientPain().run()
