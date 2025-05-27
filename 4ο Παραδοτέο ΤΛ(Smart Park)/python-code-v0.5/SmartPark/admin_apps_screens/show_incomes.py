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





class IncomesScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager

        self.add_widget(Label(text="[b]Έσοδα Πάρκινγκ[/b]", markup=True, font_size=dp(22)))

        # Επιλογή Parking
        self.add_widget(Label(text="Επιλέξτε Παρκινγκ:"))
        self.parking_spinner = Spinner(
            text="-- Επιλογή --",
            values=["Parking A", "Parking B", "Parking C"],
            size_hint_y=None,
            height=dp(44)
        )
        self.add_widget(self.parking_spinner)

        # Επιλογή Ημερομηνίας Από
        self.add_widget(Label(text="Από Ημερομηνία:"))
        self.from_spinner = Spinner(
            text="2025-05-01",
            values=["2025-05-01", "2025-05-02", "2025-05-03"],
            size_hint_y=None,
            height=dp(44)
        )
        self.add_widget(self.from_spinner)

        # Επιλογή Ημερομηνίας Έως
        self.add_widget(Label(text="Έως Ημερομηνία:"))
        self.to_spinner = Spinner(
            text="2025-05-05",
            values=["2025-05-04", "2025-05-05", "2025-05-06"],
            size_hint_y=None,
            height=dp(44)
        )
        self.add_widget(self.to_spinner)

        # Κουμπί υπολογισμού
        calc_btn = Button(
            text="Υπολογισμός Εσόδων",
            size_hint_y=None,
            height=dp(44),
            background_color=(0.3, 0.6, 0.9, 1),
            color=(1, 1, 1, 1)
        )
        calc_btn.bind(on_press=self.calculate_income)
        self.add_widget(calc_btn)

        # Label εμφάνισης αποτελέσματος
        self.result_label = Label(text="", font_size=dp(16))
        self.add_widget(self.result_label)

        # Πίσω
        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(40))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def calculate_income(self, instance):
        if self.parking_spinner.text.startswith("--"):
            self.result_label.text = "[b]Παρακαλώ επιλέξτε πάρκινγκ[/b]"
            self.result_label.markup = True
            return

        # Προσωρινός υπολογισμός με τυχαίο ποσό
        total_income = random.randint(100, 1000)
        self.result_label.text = f"[b]Σύνολο Εσόδων:[/b] {total_income}€"
        self.result_label.markup = True

    def go_back(self, instance):
        self.screen_manager.current = 'admin_home'
