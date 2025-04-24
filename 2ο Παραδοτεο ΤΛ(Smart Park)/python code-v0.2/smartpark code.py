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

        # Logo
        logo = Label(
            text="[b]SMART PARK[/b]",
            font_size=dp(24),
            markup=True,
            size_hint_y=None,
            height=dp(50))
        logo.color = (0, 0, 0)
        self.add_widget(logo)

        # κουμπί RES INFO
        res_info_btn = self.create_button("Reservation Info")
        res_info_btn.bind(on_press=self.go_to_reservation_info)
        self.add_widget(res_info_btn)

        # κουμπί tech supp
        self.add_widget(self.create_button("Technical Support"))

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


# ----------- Reservation Form Screen ------------
class ReservationFormScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager

        # Τίτλος
        self.add_widget(Label(text="[b]Ενοικίαση Θέσης Parking[/b]", markup=True, font_size=dp(20)))

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
        self.add_widget(Label(text="Ημερομηνία Έναρξης (π.χ. 2025-05-01):"))
        self.start_date_input = TextInput(
            hint_text="YYYY-MM-DD",
            size_hint_y=None,
            height=dp(44),
            multiline=False
        )
        self.add_widget(self.start_date_input)

        # Ημερομηνία Έως
        self.add_widget(Label(text="Ημερομηνία Λήξης (π.χ. 2025-05-31):"))
        self.end_date_input = TextInput(
            hint_text="YYYY-MM-DD",
            size_hint_y=None,
            height=dp(44),
            multiline=False
        )
        self.add_widget(self.end_date_input)

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

        # Αποτέλεσμα ελέγχου (προσωρινά)
        self.result_label = Label(text="", font_size=dp(14))
        self.add_widget(self.result_label)

        # Πίσω στην αρχική
        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(40))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def check_availability(self, instance):
        # Dummy logic
        self.result_label.text = "[b]Η θέση είναι διαθέσιμη![/b]"
        self.result_label.markup = True

    def go_back(self, instance):
        self.screen_manager.current = 'home'


# ----------- Profile Screen ------------
class ProfileScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager
        self.editing = False

        self.add_widget(Label(text="[b]Προφίλ Χρήστη[/b]", markup=True, font_size=dp(22)))

        # Όνομα
        self.name_label = Label(text="Όνομα: Αλβανός Δημήτριος")
        self.name_input = TextInput(text="Αλβανός Δημήτριος", multiline=False, size_hint_y=None, height=dp(40))
        self.add_widget(self.name_label)

        # Email
        self.email_label = Label(text="Email: mimis@example.com")
        self.email_input = TextInput(text="mimis@example.com", multiline=False, size_hint_y=None, height=dp(40))
        self.add_widget(self.email_label)

       

        # Κουμπί Επεξεργασίας / Αποθήκευσης
        self.edit_btn = Button(text="Edit", size_hint_y=None, height=dp(44))
        self.edit_btn.bind(on_press=self.toggle_edit)
        self.add_widget(self.edit_btn)

        # Πίσω
        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(40))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def toggle_edit(self, instance):
        self.clear_widgets()
        self.add_widget(Label(text="[b]Προφίλ Χρήστη[/b]", markup=True, font_size=dp(22)))

        if not self.editing:
            # Ενεργοποίηση επεξεργασίας
            self.add_widget(self.name_input)
            self.add_widget(self.email_input)
            self.edit_btn.text = "Save"
        else:
            # Αποθήκευση αλλαγών
            name = self.name_input.text
            email = self.email_input.text
            self.name_label.text = f"Όνομα: {name}"
            self.email_label.text = f"Email: {email}"
            self.add_widget(self.name_label)
            self.add_widget(self.email_label)
            self.add_widget(self.subscription_label)
            self.edit_btn.text = "Edit"

        self.add_widget(self.edit_btn)

        # Πίσω κουμπί
        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(40))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

        self.editing = not self.editing

    def go_back(self, instance):
        self.screen_manager.current = 'home'


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

        # Πίσω κουμπί
        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(44))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def go_back(self, instance):
        self.screen_manager.current = 'home'


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

        return sm


if __name__ == "__main__":
    SmartParkApp().run()

