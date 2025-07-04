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

