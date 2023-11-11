from kivy.lang import Builder
from kivymd.app import MDApp
from patient_muscle_upper import PatientMuscleUpper

KV = '''
FloatLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1.0  # White background color (RGBA values)
        Rectangle:
            pos: self.pos
            size: self.size


    MDLabel:
        text: "Range of motion : Lower limb"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        size_hint: 0.3, 0.1
    MDLabel:
        text: "Hip :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint: 0.3, 0.1
    MDTextField:
        id: hip_active_textfield
        hint_text: "Active range"
        multiline: True
        pos_hint: {"center_x": 0.48, "center_y": 0.7}
        size_hint: 0.1, 0.1
    MDTextField:
        id: hip_passive_textfield
        hint_text: "Passive range"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.7}
        size_hint: 0.1, 0.1
    MDLabel:
        text: "Knee :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: 0.3, 0.1
    MDTextField:
        id: knee_active_textfield
        hint_text: "Active range"
        multiline: True
        pos_hint: {"center_x": 0.48, "center_y": 0.6}
        size_hint: 0.1, 0.1
    MDTextField:
        id: knee_passive_textfield
        hint_text: "Passive range"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.6}
        size_hint: 0.1, 0.1
    MDLabel:
        text: "Ankle-Foot :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: 0.3, 0.1
    MDTextField:
        id: ankle_active_textfield
        hint_text: "Active range"
        multiline: True
        pos_hint: {"center_x": 0.48, "center_y": 0.5}
        size_hint: 0.1, 0.1
    MDTextField:
        id: ankle_passive_textfield
        hint_text: "Passive range"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.5}
        size_hint: 0.1, 0.1
    MDLabel:
        text: "Neck :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        size_hint: 0.3, 0.1
    MDTextField:
        id: neck_active_textfield
        hint_text: "Active range"
        multiline: True
        pos_hint: {"center_x": 0.48, "center_y": 0.4}
        size_hint: 0.1, 0.1
    MDTextField:
        id: neck_passive_textfield
        hint_text: "Passive range"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.4}
        size_hint: 0.1, 0.1
    MDLabel:
        text: "Trunk :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        size_hint: 0.3, 0.1
    MDTextField:
        id: trunk_active_textfield
        hint_text: "Active range"
        multiline: True
        pos_hint: {"center_x": 0.48, "center_y": 0.3}
        size_hint: 0.1, 0.1
    MDTextField:
        id: trunk_passive_textfield
        hint_text: "Passive range"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.3}
        size_hint: 0.1, 0.1  
    MDRaisedButton:
        text: "Next"
        md_bg_color: "green"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint: 0.1, 0.08
        on_press: app.next()                  
'''

class PatientRange(MDApp):
    limb_textfield_ids = {
        "Hip": ("hip_active_textfield", "hip_passive_textfield"),
        "Knee": ("knee_active_textfield", "knee_passive_textfield"),
        "Ankle-Foot": ("ankle_active_textfield", "ankle_passive_textfield"),
        "Neck": ("neck_active_textfield", "neck_passive_textfield"),
        "Trunk": ("trunk_active_textfield", "trunk_passive_textfield")
    }

    def build(self):
        return Builder.load_string(KV)

    def set_error_message(self, instance_textfield, value):
        if not instance_textfield.text.strip():
            instance_textfield.error = True
            instance_textfield.helper_text = "Required field"
        else:
            instance_textfield.error = False
            instance_textfield.helper_text = ""

    def next(self):
        
        
        for limb, (active_id, passive_id) in self.limb_textfield_ids.items():
            active_range = self.root.ids[active_id].text.strip()
            passive_range = self.root.ids[passive_id].text.strip()
            
            if not active_range:
                self.root.ids[active_id].error = True
                self.root.ids[active_id].helper_text = "Required field"
            else:
                self.root.ids[active_id].error = False
                self.root.ids[active_id].helper_text = ""
                
            if not passive_range:
                self.root.ids[passive_id].error = True
                self.root.ids[passive_id].helper_text = "Required field"
            else:
                self.root.ids[passive_id].error = False
                self.root.ids[passive_id].helper_text = ""
        
        if (
           
             all(
                not self.root.ids[active_id].error and not self.root.ids[passive_id].error
                for active_id, passive_id in self.limb_textfield_ids.values()
            )
        ):
            
        
            for limb, (active_id, passive_id) in self.limb_textfield_ids.items():
                active_range = self.root.ids[active_id].text.strip()
                passive_range = self.root.ids[passive_id].text.strip()
                print(f"Range of motion for Lower limb :: {limb}:")
                print(f"Active Range: {active_range}")
                print(f"Passive Range: {passive_range}")
            self.stop()
            PatientMuscleUpper().run()       
            
           

if __name__ == '__main__':
    PatientRange().run()
