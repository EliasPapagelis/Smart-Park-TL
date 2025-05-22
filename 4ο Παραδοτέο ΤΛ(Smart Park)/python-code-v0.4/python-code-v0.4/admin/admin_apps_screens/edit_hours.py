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



class EditHoursScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager

        self.add_widget(Label(text="[b]Ρύθμιση Ωραρίου Parking[/b]", markup=True, font_size=dp(20)))

        # Επιλογή Parking
        self.add_widget(Label(text="Parking:"))
        self.parking_spinner = Spinner(
            text='-- Επιλέξτε --',
            values=('Parking A', 'Parking B', 'Parking C'),
            size_hint_y=None,
            height=dp(44)
        )
        self.add_widget(self.parking_spinner)

        # Ώρα Έναρξης
        self.add_widget(Label(text="Ώρα Έναρξης (π.χ. 08:00):"))
        self.start_time = TextInput(multiline=False, size_hint_y=None, height=dp(44))
        self.add_widget(self.start_time)

        # Ώρα Λήξης
        self.add_widget(Label(text="Ώρα Λήξης (π.χ. 22:00):"))
        self.end_time = TextInput(multiline=False, size_hint_y=None, height=dp(44))
        self.add_widget(self.end_time)

        # Κουμπί Αποθήκευσης
        save_btn = Button(
            text="Αποθήκευση νέου ωραρίου λειτουργιάς",
            size_hint_y=None,
            height=dp(50),
            background_color=(0.3, 0.6, 0.9, 1),
            color=(1, 1, 1, 1)
        )
        save_btn.bind(on_press=self.save_hours)
        self.add_widget(save_btn)

        # Μήνυμα αποτελέσματος
        self.result_label = Label(text="", font_size=dp(14))
        self.add_widget(self.result_label)





        # Πίσω κουμπί
        back_btn = Button(
        text="Πίσω",
        size_hint_y=None,
        height=dp(44),
        background_color=(0.6, 0.6, 0.6, 1),
        color=(1, 1, 1, 1)
        )
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def save_hours(self, instance):
        parking = self.parking_spinner.text
        start = self.start_time.text
        end = self.end_time.text

        # Εδώ μπορεί να προστεθεί λογική αποθήκευσης σε βάση
        if parking != '-- Επιλέξτε --' and start and end:
            self.result_label.text = f"[b]{parking}:[/b] Νέο ωράριο {start} - {end}"
            self.result_label.markup = True
        else:
            self.result_label.text = "⚠️ Παρακαλώ συμπληρώστε όλα τα πεδία."



    def go_back(self, instance):
        self.screen_manager.current = 'admin_home'
