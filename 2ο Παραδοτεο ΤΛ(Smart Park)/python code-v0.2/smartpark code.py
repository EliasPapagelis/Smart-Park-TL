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
        tech_supp_btn = self.create_button("Technical Support")
        tech_supp_btn.bind(on_press=self.go_to_technical_support)
        self.add_widget(tech_supp_btn)

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

        

# ----------- Technical Support Screen ------------
class TechnicalSupportScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager
        self.messages = []

        # Τίτλος
        self.add_widget(Label(text="[b]Technical Support[/b]", markup=True, font_size=dp(22)))

        # Περιοχή Chat (Scrollable)
        self.chat_area = ScrollView(size_hint=(1, 0.8))
        self.chat_box = BoxLayout(orientation='vertical', size_hint_y=None)
        self.chat_box.bind(minimum_height=self.chat_box.setter('height'))
        self.chat_area.add_widget(self.chat_box)
        self.add_widget(self.chat_area)

        # Πεδίο Εισαγωγής Μηνύματος
        self.message_input = TextInput(size_hint_y=None, height=dp(40), multiline=False, hint_text="Πληκτρολογήστε το μήνυμά σας...")
        self.add_widget(self.message_input)

        # Κουμπί Αποστολής
        send_btn = Button(text="Αποστολή", size_hint_y=None, height=dp(50))
        send_btn.bind(on_press=self.send_message)
        self.add_widget(send_btn)

        # Πίσω Κουμπί
        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(40))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def send_message(self, instance):
        message = self.message_input.text
        if message.strip():
            # Προσθήκη του μηνύματος του χρήστη
            user_message = Label(text=f"[b]Εσύ:[/b] {message}", markup=True, font_size=dp(14))
            self.chat_box.add_widget(user_message)

            # Προσθήκη του μηνύματος του admin (dummy)
            admin_message = Label(text=f"[b]Admin:[/b] Ευχαριστούμε για το μήνυμά σας! Θα σας βοηθήσουμε σύντομα.", markup=True, font_size=dp(14))
            self.chat_box.add_widget(admin_message)

            # Καθαρισμός του πεδίου εισαγωγής
            self.message_input.text = ''

            # Ανάληψη κύλισης στο κάτω μέρος του chat
            self.chat_area.scroll_y = 0

    def go_back(self, instance):
        self.screen_manager.current = 'home'

        
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
           
            self.edit_btn.text = "Edit"

             # Εμφάνιση μηνύματος "Saved changes"
            saved_label = Label(
                text="[b]Saved changes[/b]",
                markup=True,
                color=(0, 0.6, 0, 1),
                font_size=dp(14),
                size_hint_y=None,
                height=dp(30)
            )
            self.add_widget(saved_label)

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

        return sm


if __name__ == "__main__":
    SmartParkApp().run()



