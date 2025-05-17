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


# ----------- RES INFO SCREEN ------------

class ReservationInfoScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager

        self.add_widget(Label(text="[b]Στοιχεία Κράτησης[/b]", markup=True, font_size=dp(22)))

        # Δημιουργία dummy δεδομένων
        reservation_data = f"Reservation ID: {random.randint(1000,9999)}\nParking: Parking A\nSpot: Θέση 2\nFrom: 2025-05-01\nTo: 2025-05-31"
        
        # Δημιουργία QR code
        qr = qrcode.make(reservation_data)
        buffer = io.BytesIO()
        qr.save(buffer, format='PNG')
        buffer.seek(0)

        # Εμφάνιση QR code στην οθόνη
        im = CoreImage(buffer, ext='png')
        qr_image = Image(texture=im.texture)
        self.add_widget(qr_image)



        # Κουμπί Πληρωμής Προστιμού
        pay_fine_btn = Button(
            text="Πληρωμή Προστιμού",
            size_hint_y=None,
            height=dp(50),
            background_color=(1, 0.3, 0.3, 1),
            color=(1, 1, 1, 1)
        )

        self.add_widget(pay_fine_btn)
      
      

        # Κουμπί Ακύρωσης Κράτησης
        cancel_btn = Button(
            text="Ακύρωση Κράτησης",
            size_hint_y=None,
            height=dp(50),
            background_color=(1, 0.3, 0.3, 1),  # Κόκκινο για την ακύρωση
            color=(1, 1, 1, 1)
        )
        cancel_btn.bind(on_press=self.cancel_reservation)
        self.add_widget(cancel_btn)

     

        # Πίσω κουμπί
        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(44))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)



    def cancel_reservation(self, instance):
        # Εδώ διαγράφουμε τα δεδομένα κράτησης 
        self.reservation_data = None  # Διαγραφή των δεδομένων
        self.clear_widgets()  # Καθαρισμός των widgets

        # Εμφάνιση μηνύματος ακύρωσης
        cancel_message = Label(
            text="[b]Reservation Cancelled[/b]",
            markup=True,
            font_size=dp(18),
            color=(0.8, 0, 0, 1),
            size_hint_y=None,
            height=dp(30)
        )
        self.add_widget(cancel_message)

        # Πίσω κουμπί για να επιστρέψει ο χρήστης στην αρχική οθόνη
        back_btn = Button(
            text="Πίσω στην Αρχική",
            size_hint_y=None,
            height=dp(44),
            background_color=(0.3, 0.6, 0.9, 1),
            color=(1, 1, 1, 1)
        )
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

 

    def go_back(self, instance):
        self.screen_manager.current = 'home'
