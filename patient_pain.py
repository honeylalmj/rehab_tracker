from kivy.lang import Builder
from kivymd.app import MDApp
from patient_range import PatientRange

KV = '''
FloatLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1.0  # White background color (RGBA values)
        Rectangle:
            pos: self.pos
            size: self.size

    MDLabel:
        text: "Pain assessment : "
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        size_hint: 0.3, 0.1

    MDSwitch:
        id: yes_switch
        on_active: app.toggle_textfield("Yes", self.active)
        pos_hint: {"center_x": 0.52, "center_y": 0.9}

    MDLabel:
        text: "Yes"
        pos_hint: {"center_x": 0.62, "center_y": 0.9}
        size_hint: 0.3, 0.1

    MDSwitch:
        id: no_switch
        on_active: app.toggle_textfield("No", self.active)
        pos_hint: {"center_x": 0.62, "center_y": 0.9}

    MDLabel:
        text: "No"
        pos_hint: {"center_x": 0.72, "center_y": 0.9}
        size_hint: 0.3, 0.1

    MDTextField:
        id: assessment_textfield
        hint_text: "VAS between 0 - 10"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        size_hint: 0.3, 0.1
    MDLabel:
        text: "Range of motion : Upper limb"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint: 0.3, 0.1
    MDLabel:
        text: "Shoulder :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: 0.3, 0.1
    MDTextField:
        id: shoulder_active_textfield
        hint_text: "Active range"
        multiline: True
        pos_hint: {"center_x": 0.48, "center_y": 0.6}
        size_hint: 0.1, 0.1
    MDTextField:
        id: shoulder_passive_textfield
        hint_text: "Passive range"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.6}
        size_hint: 0.1, 0.1
    MDLabel:
        text: "Elbow :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: 0.3, 0.1
    MDTextField:
        id: elbow_active_textfield
        hint_text: "Active range"
        multiline: True
        pos_hint: {"center_x": 0.48, "center_y": 0.5}
        size_hint: 0.1, 0.1
    MDTextField:
        id: elbow_passive_textfield
        hint_text: "Passive range"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.5}
        size_hint: 0.1, 0.1
    MDLabel:
        text: "Forearm :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        size_hint: 0.3, 0.1
    MDTextField:
        id: forearm_active_textfield
        hint_text: "Active range"
        multiline: True
        pos_hint: {"center_x": 0.48, "center_y": 0.4}
        size_hint: 0.1, 0.1
    MDTextField:
        id: forearm_passive_textfield
        hint_text: "Passive range"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.4}
        size_hint: 0.1, 0.1
    MDLabel:
        text: "Wrist :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        size_hint: 0.3, 0.1
    MDTextField:
        id: wrist_active_textfield
        hint_text: "Active range"
        multiline: True
        pos_hint: {"center_x": 0.48, "center_y": 0.3}
        size_hint: 0.1, 0.1
    MDTextField:
        id: wrist_passive_textfield
        hint_text: "Passive range"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.3}
        size_hint: 0.1, 0.1
    MDLabel:
        text: "Fingers :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint: 0.3, 0.1
    MDTextField:
        id: finger_active_textfield
        hint_text: "Active range"
        multiline: True
        pos_hint: {"center_x": 0.48, "center_y": 0.2}
        size_hint: 0.1, 0.1
    MDTextField:
        id: finger_passive_textfield
        hint_text: "Passive range"
        multiline: True
        pos_hint: {"center_x": 0.6, "center_y": 0.2}
        size_hint: 0.1, 0.1  
    MDRaisedButton:
        text: "Next"
        md_bg_color: "green"
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        size_hint: 0.1, 0.08
        on_press: app.next()                  
'''

class PatientPain(MDApp):
    limb_textfield_ids = {
        "Shoulder": ("shoulder_active_textfield", "shoulder_passive_textfield"),
        "Elbow": ("elbow_active_textfield", "elbow_passive_textfield"),
        "Forearm": ("forearm_active_textfield", "forearm_passive_textfield"),
        "Wrist": ("wrist_active_textfield", "wrist_passive_textfield"),
        "Fingers": ("finger_active_textfield", "finger_passive_textfield"),
    }

    def build(self):
        return Builder.load_string(KV)

    def toggle_textfield(self, pain_assessment_type, switch_active):
        textfield = self.root.ids.assessment_textfield
        if pain_assessment_type == "Yes" and switch_active:
            textfield.disabled = False
            self.root.ids.no_switch.active = False
        elif pain_assessment_type == "No" and switch_active:
            textfield.disabled = True
            self.root.ids.yes_switch.active = False

    def set_error_message(self, instance_textfield, value):
        if not instance_textfield.text.strip():
            instance_textfield.error = True
            instance_textfield.helper_text = "Required field"
        else:
            instance_textfield.error = False
            instance_textfield.helper_text = ""

    
    def next(self):
        assessment_text = self.root.ids.assessment_textfield.text.strip()
        all_fields_filled = True
        

        # Check if "Yes" is selected, and the assessment text is empty
        if self.root.ids.yes_switch.active and not assessment_text:
            self.root.ids.assessment_textfield.error = True
            self.root.ids.assessment_textfield.helper_text = "Required field"
            all_fields_filled = False
        else:
            # If "No" is selected, clear any previous error messages
            self.root.ids.assessment_textfield.error = False
            self.root.ids.assessment_textfield.helper_text = ""

        # Check if all limb range text fields are filled
        for limb, (active_id, passive_id) in self.limb_textfield_ids.items():
            active_range = self.root.ids[active_id].text.strip()
            passive_range = self.root.ids[passive_id].text.strip()

            if not active_range or not passive_range:
                all_fields_filled = False

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

        # Print the input if all fields are filled
        if all_fields_filled:
            if self.root.ids.no_switch.active:
                print("Pain Assessment: 0")
            else:
                print(f"Pain Assessment: {assessment_text}")

            for limb, (active_id, passive_id) in self.limb_textfield_ids.items():
                active_range = self.root.ids[active_id].text.strip()
                passive_range = self.root.ids[passive_id].text.strip()
                print(f"Range of motion for Upper limb :: {limb}:")
                print(f"Active Range: {active_range}")
                print(f"Passive Range: {passive_range}")
            self.stop()
            PatientRange().run()        

if __name__ == '__main__':
    PatientPain().run()
