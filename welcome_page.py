from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

class MainApp(MDApp):
    def build(self):
        screen = MDScreen()
        # Lavender background for the screen (RGB values as floats)
        screen.md_bg_color = (0.784, 0.784, 0.941, 1.0)

        layout = MDBoxLayout(orientation='vertical')
        # Background color for the layout (RGB values as floats)
        layout.md_bg_color = (0.784, 0.784, 0.941, 1.0)
        

        label = MDLabel(text="Rehab Tracker", halign="center")
        layout.add_widget(label)

        screen.add_widget(layout)

        return screen

if __name__ == "__main__":
    MainApp().run()
