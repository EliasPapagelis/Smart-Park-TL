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


# ----------- Rent a Spot Screen ------------
class RentSpotScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager

        # Τίτλος
        self.add_widget(Label(text="[b]Ενοικίαση Θέσης Parking (Rent a Spot)[/b]", markup=True, font_size=dp(20)))

        # Επιλογή Παρκινγκ
        self.add_widget(Label(text="Επιλογή Παρκινγκ:"))
        self.parking_spinner = Spinner(
            text='-- Επιλέξτε --',
            values=('Parking A', 'Parking B', 'Parking C'),
            size_hint_y=None,
            height=dp(44)
        )
        self.add_widget(self.parking_spinner)

        # Επιλογή Θέσης
        self.add_widget(Label(text="Επιλογή Θέσης:"))
        self.spot_spinner = Spinner(
            text='-- Επιλέξτε --',
            values=('Θέση 1', 'Θέση 2', 'Θέση 3'),
            size_hint_y=None,
            height=dp(44)
        )
        self.add_widget(self.spot_spinner)

        # Ημερομηνία Από
        self.add_widget(Label(text="Ημερομηνία Έναρξης (π.χ. 2025-06-01):"))
        self.start_date_input = TextInput(
            hint_text="YYYY-MM-DD",
            size_hint_y=None,
            height=dp(44),
            multiline=False
        )
        self.add_widget(self.start_date_input)

        # Ημερομηνία Έως
        self.add_widget(Label(text="Ημερομηνία Λήξης (π.χ. 2025-06-10):"))
        self.end_date_input = TextInput(
            hint_text="YYYY-MM-DD",
            size_hint_y=None,
            height=dp(44),
            multiline=False
        )
        self.add_widget(self.end_date_input)

        # Κουμπί Ενοικίασης
        self.rent_btn = Button(
            text="Ενοικίαση",
            size_hint_y=None,
            height=dp(50),
            background_color=(0.1, 0.7, 0.3, 1),
            color=(1, 1, 1, 1)
        )
        self.rent_btn.bind(on_press=self.rent_spot)
        self.add_widget(self.rent_btn)

        # Αποτέλεσμα
        self.result_label = Label(text="", font_size=dp(14))
        self.add_widget(self.result_label)

        # Πίσω στην αρχική
        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(40))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def rent_spot(self, instance):
        # Dummy ενοικίαση (μπορείς αργότερα να βάλεις αποθήκευση σε αρχείο κ.λπ.)
        self.result_label.text = "[b]Η κράτηση ολοκληρώθηκε με επιτυχία![/b]"
        self.result_label.markup = True

    def go_back(self, instance):
        self.screen_manager.current = 'home'
