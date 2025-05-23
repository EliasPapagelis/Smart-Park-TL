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
from database import is_spot_available, save_reservation
from datetime import datetime, timedelta



# ----------- Reservation Form Screen ------------
class ReservationFormScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager

        # Τίτλος
        self.add_widget(Label(text="[b]Κράτηση Θέσης Parking[/b]", markup=True, font_size=dp(20)))

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




        # Δημιουργία dummy διαθέσιμων ημερομηνιών (π.χ. επόμενες 7 ημέρες)
        today = datetime.now()
        available_dates = [(today + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(1, 8)]


        # Spinner για ημερομηνία έναρξης
        self.add_widget(Label(text="Ημερομηνία Έναρξης:"))
        self.start_date_spinner = Spinner(
        text="-- Επιλέξτε --",
        values=available_dates,
        size_hint_y=None,
        height=dp(44)
        )
        self.add_widget(self.start_date_spinner)

        # Spinner για ημερομηνία λήξης
        self.add_widget(Label(text="Ημερομηνία Λήξης:"))
        self.end_date_spinner = Spinner(
        text="-- Επιλέξτε --",
        values=available_dates,
        size_hint_y=None,
        height=dp(44)
        )
        self.add_widget(self.end_date_spinner)

        # Κουμπί Ελέγχου Διαθεσιμότητας
        self.check_btn = Button(
            text="Έλεγχος Διαθεσιμότητας",
            size_hint_y=None,
            height=dp(50),
            background_color=(0.3, 0.6, 0.9, 1),
            color=(1, 1, 1, 1)
        )
        self.check_btn.bind(on_press=self.check_availability)
        self.add_widget(self.check_btn)
         # Κουμπί Ενοικίασης
        self.book_btn = Button(
            text="Κράτηση",
            size_hint_y=None,
            height=dp(50),
            background_color=(0.3, 0.6, 0.9, 1),
            color=(1, 1, 1, 1)
        )
        self.book_btn.bind(on_press=self.make_reservation)
        self.book_btn.disabled = True  # θα ενεργοποιηθεί μετά τον έλεγχο
        self.add_widget(self.book_btn)

        # Αποτέλεσμα ελέγχου (προσωρινά)
        self.result_label = Label(text="", font_size=dp(14))
        self.add_widget(self.result_label)

        # Πίσω στην αρχική
        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(40))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def check_availability(self, instance):
        parking = self.parking_spinner.text
        spot = self.spot_spinner.text
        date_from = self.start_date_spinner.text
        date_to= self.end_date_spinner.text


        if is_spot_available(parking, spot, date_from, date_to):
         self.result_label.text = "[b]Η θέση είναι διαθέσιμη![/b]"
         self.result_label.markup = True
         self.book_btn.disabled = False
        else:
         self.result_label.text = "[b]Η θέση δεν είναι διαθέσιμη για τις επιλεγμένες ημερομηνίες.[/b]"
         self.result_label.markup = True

    def go_back(self, instance):
        self.screen_manager.current = 'home'



    def make_reservation(self, instance):
        parking = self.parking_spinner.text
        spot = self.spot_spinner.text
        date_from = self.start_date_spinner.text
        date_to= self.end_date_spinner.text


        if is_spot_available(parking, spot, date_from, date_to):
         save_reservation(parking, spot, date_from, date_to)
         self.result_label.text = "[b]Η κράτηση ολοκληρώθηκε με επιτυχία![/b]"
         self.result_label.markup = True
        else:
         self.result_label.text = "[b]Η θέση είναι ήδη δεσμευμένη.[/b]"
         self.result_label.markup = True

