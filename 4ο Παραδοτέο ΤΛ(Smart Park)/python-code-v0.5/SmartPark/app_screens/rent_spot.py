from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label     import Label
from kivy.uix.spinner   import Spinner
from kivy.uix.button    import Button
from kivy.metrics       import dp

from database import is_spot_available, save_reservation

class RentSpotScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager

        # Τίτλος
        self.add_widget(Label(
            text="[b]Ενοικίαση Θέσης Parking (Rent a Spot)[/b]",
            markup=True, font_size=dp(20)
        ))

        # Επιλογή Parking
        self.add_widget(Label(text="Επιλογή Parking:"))
        self.parking_spinner = Spinner(
            text='-- Επιλέξτε --',
            values=('Parking A', 'Parking B', 'Parking C'),
            size_hint_y=None, height=dp(44)
        )
        self.add_widget(self.parking_spinner)

        # Επιλογή Spot
        self.add_widget(Label(text="Επιλογή Θέσης:"))
        self.spot_spinner = Spinner(
            text='-- Επιλέξτε --',
            values=('Θέση 1', 'Θέση 2', 'Θέση 3'),
            size_hint_y=None, height=dp(44)
        )
        self.add_widget(self.spot_spinner)

        # Ημερομηνία Από
        self.add_widget(Label(text="Ημερομηνία Έναρξης:"))
        self.start_date_spinner = Spinner(
            text='2025-06-01',
            values=('2025-06-01', '2025-06-02', '2025-06-03'),
            size_hint_y=None, height=dp(44)
        )
        self.add_widget(self.start_date_spinner)

        # Ημερομηνία Έως
        self.add_widget(Label(text="Ημερομηνία Λήξης:"))
        self.end_date_spinner = Spinner(
            text='2025-06-05',
            values=('2025-06-04', '2025-06-05', '2025-06-06'),
            size_hint_y=None, height=dp(44)
        )
        self.add_widget(self.end_date_spinner)

        # Κουμπί Έλεγχος Διαθεσιμότητας
        check_btn = Button(
            text="Έλεγχος Διαθεσιμότητας",
            size_hint_y=None, height=dp(50),
            background_color=(0.3, 0.6, 0.9, 1), color=(1,1,1,1)
        )
        check_btn.bind(on_press=self.check_availability)
        self.add_widget(check_btn)

        # Κουμπί Ενοικίασης
        self.rent_btn = Button(
            text="Ενοικίαση",
            size_hint_y=None, height=dp(50),
            background_color=(0.1, 0.7, 0.3, 1), color=(1,1,1,1)
        )
        self.rent_btn.bind(on_press=self.do_rent)
        self.rent_btn.disabled = True  # θα ενεργοποιηθεί μετά τον έλεγχο
        self.add_widget(self.rent_btn)

        # Ετικέτα αποτελέσματος
        self.result_label = Label(text="", font_size=dp(14))
        self.add_widget(self.result_label)

        # Πίσω στην Αρχική
        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(40))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def check_availability(self, instance):
        parking   = self.parking_spinner.text
        spot      = self.spot_spinner.text
        date_from = self.start_date_spinner.text
        date_to   = self.end_date_spinner.text

        if parking.startswith("--") or spot.startswith("--"):
            self.result_label.text = "[b]️ Επιλέξτε Parking και Θέση πρώτα.[/b]"
            self.result_label.markup = True
            return

        available = is_spot_available(parking, spot, date_from, date_to)
        if available:
            self.result_label.text = "[b] Διαθέσιμη![/b]"
            self.rent_btn.disabled = False
        else:
            self.result_label.text = "[b] Δεν είναι διαθέσιμη σε αυτές τις ημερομηνίες.[/b]"
            self.rent_btn.disabled = True
        self.result_label.markup = True

    def do_rent(self, instance):
        parking   = self.parking_spinner.text
        spot      = self.spot_spinner.text
        date_from = self.start_date_spinner.text
        date_to   = self.end_date_spinner.text

        save_reservation(parking, spot, date_from, date_to)
        self.result_label.text = "[b]✅ Η κράτηση ολοκληρώθηκε με επιτυχία![/b]"
        self.result_label.markup = True
        self.rent_btn.disabled = True

    def go_back(self, instance):
        self.screen_manager.current = 'home'
