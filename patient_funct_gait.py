from kivy.lang import Builder
from kivymd.app import MDApp
from patient_treatment import PatientTreatment


KV = '''
FloatLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1.0  # White background color (RGBA values)
        Rectangle:
            pos: self.pos
            size: self.size
    
    MDLabel:
        text: "Functional evaluation :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.75, "center_y": 0.8}
   
    

    MDTextField:
        id: balance_textfield
        hint_text: "Balance"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint: 0.5, 0.1
         
    MDTextField:
        id: coordination_textfield
        hint_text: "Coordination"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: 0.5, 0.1
    MDLabel:
        text: "Gait analysis :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.75, "center_y": 0.49}    
    MDTextField:
        id: gait_textfield
        hint_text: ""
        multiline: True
        pos_hint: {"center_x": 0.55, "center_y": 0.5}
        size_hint: 0.4, 0.1
    MDLabel:
        text: "Activity limitations :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.75, "center_y": 0.4}    
    MDTextField:
        id: activity_textfield
        hint_text: ""
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



class PatientFunctGait(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        
  

    def set_item(self, text_item):
        self.screen.ids.drop_item.text = text_item
        self.menu.dismiss()     

    def build(self):
        self.screen.ids.balance_textfield.bind(
            on_text=self.set_error_message,
        )
        self.screen.ids.coordination_textfield.bind(
            on_text=self.set_error_message,
        )
        self.screen.ids.gait_textfield.bind(
            on_text=self.set_error_message, 
        )
        self.screen.ids.activity_textfield.bind(
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
       
        balance = self.screen.ids.balance_textfield.text.strip()
        coordination = self.screen.ids.coordination_textfield.text.strip()
        gait_analysis = self.screen.ids.gait_textfield.text.strip()
        activity = self.screen.ids.activity_textfield.text.strip()

        # Reset error messages for all fields
       
        self.screen.ids.balance_textfield.error = False
        self.screen.ids.coordination_textfield.error = False
        self.screen.ids.gait_textfield.error = False
        self.screen.ids.activity_textfield.error = False

     

        if not balance:
            self.screen.ids.balance_textfield.error = True
            self.screen.ids.balance_textfield.helper_text = "Required field"

        if not coordination:
            self.screen.ids.coordination_textfield.error = True
            self.screen.ids.coordination_textfield.helper_text = "Required field"

        if not gait_analysis:
            self.screen.ids.gait_textfield.error = True
            self.screen.ids.gait_textfield.helper_text = "Required field"

        if not activity:
            self.screen.ids.activity_textfield.error = True
            self.screen.ids.activity_textfield.helper_text = "Required field"
        
        if (
            balance
            and coordination
            and gait_analysis
            and activity
        ):
            # Implement your logic to process the input data here
            # For example, you can print the input data
            print(f"Functional evaluation :: Balance: {balance}")
            print(f"Functional evaluation :: Coordination: {coordination}")
            print(f"Gait anaylysis : {gait_analysis}")
            print(f"Activity limitations : {activity}")
            self.stop()
            PatientTreatment().run()    
            
if __name__ == "__main__":
    PatientFunctGait().run()
