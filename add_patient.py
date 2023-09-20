from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"

        screen = MDScreen(md_bg_color=(0.784, 0.784, 0.941, 1.0))  # Lavender background color (RGBA values)
        screen.add_widget(
            MDRectangleFlatIconButton(
                text="Add Patient",
                icon="account-plus-outline",
                line_color=(0, 0, 0, 0),
                pos_hint={"center_x": .5, "center_y": 0.6},
            )
        )
        screen.add_widget(
            MDRectangleFlatIconButton(
                text="View Patient",
                icon="eye",
                line_color=(0, 0, 0, 0),
                pos_hint={"center_x": .5, "center_y": 0.5},  # Adjusted Y position
            )
        )

        return screen

if __name__ == "__main__":
    Example().run()
