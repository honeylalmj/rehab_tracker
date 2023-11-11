from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

class MainApp(MDApp):
    def build(self):
        screen = MDScreen()
        # Set the background color to white (RGB values as floats)
        screen.md_bg_color = (1, 1, 1, 1)  # White background color

        layout = MDBoxLayout(orientation='vertical')
        # Set the background color for the layout to white (RGB values as floats)
        layout.md_bg_color = (1, 1, 1, 1)  # White background color

        label = MDLabel(text="Rehab Tracker", halign="center")
        layout.add_widget(label)

        screen.add_widget(layout)

        return screen

if __name__ == "__main__":
    MainApp().run()
