from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.metrics import dp
from kivy.core.window import Window

class CreateAccountScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=[dp(30), dp(20)], spacing=dp(15), **kwargs)
        
        # Background 
        with self.canvas.before:
            Color(1, 1, 1, 1)  
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        # Logo 
        self.add_widget(Label(
            text="[b]SMART PARK[/b]",
            font_size=dp(28),
            markup=True,
            size_hint_y=None,
            height=dp(60),
            color=(0, 0, 0)))  

        # Input fields 
        field_style = {
            'size_hint_y': None,
            'height': dp(50),
            'background_color': (0.68, 0.85, 0.9, 1),  
            'foreground_color': (0, 0, 0, 1),  
            'hint_text_color': (0.5, 0.5, 0.5, 1),
            'padding': [dp(15), dp(15)],
            'multiline': False
        }

        self.username = TextInput(hint_text='Username', **field_style)
        self.add_widget(self.username)

        self.email = TextInput(hint_text='Email', **field_style)
        self.add_widget(self.email)

        self.password = TextInput(hint_text='Password', password=True, **field_style)
        self.add_widget(self.password)

        self.confirm_password = TextInput(hint_text='Confirm Password', password=True, **field_style)
        self.add_widget(self.confirm_password)

        # Button 
        self.create_account_btn = Button(
            text='CREATE ACCOUNT',
            size_hint_y=None,
            height=dp(55),
            background_color=(0, 0.7, 0, 1), 
            color=(1, 1, 1, 1), 
            bold=True,
            font_size=dp(18),
            background_normal='')  
        self.create_account_btn.bind(on_press=self.create_account)
        self.add_widget(self.create_account_btn)

        # Tagline (διορθωμένο)
        self.add_widget(Label(
            text="Easy, fast and smart way to park your vehicle",
            font_size=dp(14),
            color=(0, 0, 0),  
            size_hint_y=None,
            height=dp(30)))

    def create_account(self, instance):
        print(f"Creating account for {self.username.text}")

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

class SmartParkApp(App):
    def build(self):
        Window.size = (360, 640)  
        return CreateAccountScreen()

if __name__ == "__main__":
    SmartParkApp().run()

