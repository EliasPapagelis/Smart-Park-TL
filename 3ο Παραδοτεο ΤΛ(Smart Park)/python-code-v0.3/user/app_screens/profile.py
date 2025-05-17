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
