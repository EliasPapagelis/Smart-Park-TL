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



# ----------- Home Screen ------------
class HomeScreen(BoxLayout):
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
            text="[b]SMART PARK[/b]",
            font_size=dp(24),
            markup=True,
            size_hint_y=None,
            height=dp(50))
        logo.color = (0, 0, 0)
        self.add_widget(logo)

       
        # κουμπί rent a spot
        rent_spot_btn = self.create_button("Rent a spot")
        rent_spot_btn.bind(on_press=self.go_to_rent_spot)
        self.add_widget(rent_spot_btn)

        # κουμπί tech supp
        tech_supp_btn = self.create_button("Technical Support")
        tech_supp_btn.bind(on_press=self.go_to_technical_support)
        self.add_widget(tech_supp_btn)

        # κουμπί RES INFO 
        res_info_btn = self.create_button("Reservation Info")
        res_info_btn.bind(on_press=self.go_to_reservation_info)
        self.add_widget(res_info_btn)



        # κουμπί Profile
        profile_btn = self.create_button("Profile")
        profile_btn.bind(on_press=self.go_to_profile)
        self.add_widget(profile_btn)
        #self.add_widget(Widget(size_hint_y=None, height=dp(20)))

        # MAKE RESERVATION Button
        self.make_reservation_btn = Button(
            text='MAKE RESERVATION',
            size_hint_y=None,
            height=dp(60),
            background_normal='',
            background_color=(0.68, 0.85, 0.9, 1),
            color=(1, 1, 1, 1),
            bold=True,
            font_size=dp(18))
        self.make_reservation_btn.bind(on_press=self.go_to_reservation_form)
        self.add_widget(self.make_reservation_btn)

        self.add_widget(Widget(size_hint_y=None, height=dp(20)))

        # Tagline
        tagline = Label(
            text="Easy, fast and smart way to park your vehicle",
            font_size=dp(14),
            size_hint_y=None,
            height=dp(30))
        tagline.color = (0, 0, 0)
        self.add_widget(tagline)

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

    def go_to_reservation_form(self, instance):
        self.screen_manager.current = 'reservation_form'

    def go_to_profile(self, instance):
        self.screen_manager.current = 'profile'

    def go_to_reservation_info(self, instance):
        self.screen_manager.current = 'reservation_info'

    def go_to_technical_support(self, instance):
        self.screen_manager.current = 'technical_support'

    def go_to_rent_spot(self, instance):
        self.screen_manager.current = 'rent_spot'
