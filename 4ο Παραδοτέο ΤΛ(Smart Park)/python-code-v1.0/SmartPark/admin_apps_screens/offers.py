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



class OffersScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager
        self.offers = {}

        self.add_widget(Label(text="[b]Διαχείριση Προσφορών[/b]", markup=True, font_size=dp(22)))

        # Επιλογή Parking
        self.add_widget(Label(text="Επιλογή Παρκινγκ:"))
        self.parking_spinner = Spinner(
            text='-- Επιλέξτε Παρκινγκ --',
            values=('Parking A', 'Parking B', 'Parking C'),
            size_hint_y=None,
            height=dp(44)
        )
        self.parking_spinner.bind(text=self.load_offers)
        self.add_widget(self.parking_spinner)

        # Λίστα Προσφορών
        self.offers_label = Label(text="Προσφορές:\n-", font_size=dp(16))
        self.add_widget(self.offers_label)

        # Νέα προσφορά
        self.add_widget(Label(text="Νέα Προσφορά:"))
        self.offer_input = TextInput(hint_text="π.χ. -20% σε βραδινές ώρες", size_hint_y=None, height=dp(40))
        self.add_widget(self.offer_input)

        # Προσθήκη προσφοράς
        add_btn = Button(text="Προσθήκη Προσφοράς", size_hint_y=None, height=dp(40))
        add_btn.bind(on_press=self.add_offer)
        self.add_widget(add_btn)

        # Αποθήκευση
        save_btn = Button(text="Αποθήκευση", size_hint_y=None, height=dp(40))
        save_btn.bind(on_press=self.save_offers)
        self.add_widget(save_btn)

        # Πίσω
        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(40))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

        self.offers_data = {}

    def load_offers(self, spinner, text):
        offers = self.offers_data.get(text, ["-"])
        self.offers_label.text = f"Προσφορές για {text}:\n" + "\n".join(offers)

    def add_offer(self, instance):
        parking = self.parking_spinner.text
        offer = self.offer_input.text.strip()
        if parking.startswith('--') or not offer:
            return
        self.offers_data.setdefault(parking, []).append(offer)
        self.offer_input.text = ""
        self.load_offers(None, parking)

    def save_offers(self, instance):
        print("Αποθηκεύτηκαν οι προσφορές:", self.offers_data)

    def go_back(self, instance):
        self.screen_manager.current = 'admin_home'
