from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivy.core.window import Window
from patient_personal_details import PatientPersonalDetails
KV = '''
FloatLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1.0  # White background color (RGBA values)
        Rectangle:
            pos: self.pos
            size: self.size
    MDIcon:
        icon: "account-plus-outline"
        pos_hint: {"center_x": .5, "center_y": .7}
        font_size: "36sp"
    MDIcon:
        icon: "eye"
        pos_hint: {"center_x": .5, "center_y": .5}
        font_size: "36sp"
    MDRaisedButton:
        text: "Add patient"
        md_bg_color: "green"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint:0.1, 0.08
        on_press : app.add_patient_login()
    MDRaisedButton:
        text: "View Patient"
        md_bg_color: "green"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        size_hint:0.1, 0.08
        on_press : view.login()        
          
    

        '''

class AddPatient(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        
        
    def build(self):
        return self.screen
    
    def add_patient_login(self) :
        self.stop()
        PatientPersonalDetails().run()


        
     

if __name__ == "__main__":
    AddPatient().run()