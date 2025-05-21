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
from app_screens.home import HomeScreen
from app_screens.reservation_form import ReservationFormScreen
from app_screens.profile import ProfileScreen
from app_screens.reservation_info import ReservationInfoScreen
from app_screens.technical_support import TechnicalSupportScreen
from app_screens.rent_spot import RentSpotScreen
from database import init_db



# ----------- Main App ------------
class SmartParkApp(App):
    def build(self):
        Window.size = (360, 640)
        sm = ScreenManager()

        # Home screen
        home_screen = Screen(name='home')
        home_screen.add_widget(HomeScreen(sm))
        sm.add_widget(home_screen)

        # Reservation form screen
        form_screen = Screen(name='reservation_form')
        form_screen.add_widget(ReservationFormScreen(sm))
        sm.add_widget(form_screen)

        # Profile screen
        profile_screen = Screen(name='profile')
        profile_screen.add_widget(ProfileScreen(sm))
        sm.add_widget(profile_screen)

        # Reservation Info screen
        info_screen = Screen(name='reservation_info')
        info_screen.add_widget(ReservationInfoScreen(sm))
        sm.add_widget(info_screen)

        # Technical Support screen
        tech_support_screen = Screen(name='technical_support')
        tech_support_screen.add_widget(TechnicalSupportScreen(sm))
        sm.add_widget(tech_support_screen)

        # Rent a spot screen
        rent_spot_screen = Screen(name='rent_spot')
        rent_spot_screen.add_widget(RentSpotScreen(sm))
        sm.add_widget(rent_spot_screen)

        return sm




if __name__ == "__main__":
    init_db()
    SmartParkApp().run()
