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
from database import get_last_reservation, delete_last_reservation


# ----------- RES INFO SCREEN ------------

class ReservationInfoScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager

        self.add_widget(Label(text="[b]Στοιχεία Κράτησης[/b]", markup=True, font_size=dp(22)))

        reservation = get_last_reservation()
        if reservation:
            res_id, parking, spot, start_date, end_date, status = reservation
            reservation_data = f"Reservation ID: {res_id}\nParking: {parking}\nSpot: {spot}\nFrom: {start_date}\nTo: {end_date}"

            qr = qrcode.make(reservation_data)
            buffer = io.BytesIO()
            qr.save(buffer, format='PNG')
            buffer.seek(0)

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
            pay_fine_btn.bind(on_press=self.go_to_payment)

            # Κουμπί Ακύρωσης Κράτησης
            cancel_btn = Button(
                text="Ακύρωση Κράτησης",
                size_hint_y=None,
                height=dp(50),
                background_color=(1, 0.3, 0.3, 1),
                color=(1, 1, 1, 1)
            )
            cancel_btn.bind(on_press=self.cancel_reservation)
            self.add_widget(cancel_btn)
        else:
            self.add_widget(Label(text="Δεν υπάρχουν κρατήσεις."))

        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(44))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def cancel_reservation(self, instance):
        delete_last_reservation()
        self.clear_widgets()
        self.add_widget(Label(text="[b]Reservation Cancelled[/b]", markup=True, font_size=dp(18)))
        back_btn = Button(text="Πίσω στην Αρχική", size_hint_y=None, height=dp(44))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def go_back(self, instance):
        self.screen_manager.current = 'home'


    def go_to_payment(self, instance):
        self.screen_manager.current = 'payment'
   
