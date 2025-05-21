from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.metrics import dp
import qrcode
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
import io
import random
from kivy.uix.scrollview import ScrollView






# ---------- Αρχική Σελίδα Διαχειριστή ----------
class AdminHomeScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager

        # Background
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)




         # Logo (εικόνα)
        logo_image = Image(
        source='logo.png',  # Αν είναι σε φάκελο: 'images/logo.png'
        size_hint=(1, None),
        height=dp(120),
        allow_stretch=True,
        keep_ratio=True
        )
        self.add_widget(logo_image)




       # Label
        logo = Label(
            text="[b]ADMIN PANEL[/b]",
            font_size=dp(24),
            markup=True,
            size_hint_y=None,
            height=dp(50))
        logo.color = (0, 0, 0)
        self.add_widget(logo)

        # Show Incomes
        income_btn = self.create_button("Show Incomes")
        income_btn.bind(on_press=self.go_to_incomes)
        self.add_widget(income_btn)

        # Edit Parking Hours
        edit_hours_btn =  self.create_button("Edit Parking Hours")
        edit_hours_btn.bind(on_press=self.go_to_edit_hours)
        self.add_widget(edit_hours_btn)

        # Offers
        offers_btn =  self.create_button("Offers")
        offers_btn.bind(on_press=self.go_to_offers)
        self.add_widget(offers_btn)

        # Technical Support
        tech_btn =  self.create_button("Technical Support")
        tech_btn.bind(on_press=self.go_to_tech_support)
        self.add_widget(tech_btn)


    def create_button(self, text):
        return Button(
            text=text,
            size_hint_y=None,
            height=dp(50),
            background_normal='',
            background_color=(0.68, 0.85, 0.9, 1),
            color=(0, 0, 0, 1)
        )



    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size



    def go_to_incomes(self, instance):
        self.screen_manager.current = 'incomes'

    def go_to_edit_hours(self, instance):
        self.screen_manager.current = 'edit_hours'

    def go_to_offers(self, instance):
        self.screen_manager.current = 'offers'

    def go_to_tech_support(self, instance):
        self.screen_manager.current = 'tech_support'
