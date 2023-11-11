from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivymd.uix.list import OneLineIconListItem
from kivy.properties import StringProperty

KV = '''
FloatLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1.0  # White background color (RGBA values)
        Rectangle:
            pos: self.pos
            size: self.size
    
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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
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

    def set_error_message(self, instance_textfield, value):
        if not instance_textfield.text.strip() or (instance_textfield == self.screen.ids.drop_item and value == "select"):
            instance_textfield.error = True
            instance_textfield.helper_text = "Required field"
        else:
            instance_textfield.error = False
            instance_textfield.helper_text = ""

    def next(self):
        # Check if any of the required fields are empty
       
        short_term_plan = self.screen.ids.shortplan_textfield.text
        long_term_plan = self.screen.ids.longplan_textfield.text
        treatment = self.screen.ids.treatment_textfield.text
        prognosis = self.screen.ids.drop_item.text
       

        # Reset error messages for all fields
       
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
            # Implement your logic to process the input data here
            # For example, you can print the input data
            print(f"Treatment plan :: Short term goal: {short_term_plan}")
            print(f"Treatment plan :: Long term goal: {long_term_plan}")
            print(f"Treatment : {treatment}")
            print(f"Prognosis : {prognosis}")
            self.stop()    
            
if __name__ == "__main__":
    PatientTreatment().run()
