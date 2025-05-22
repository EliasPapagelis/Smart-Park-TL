from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import dp
import re

class ProfileScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager
        self.editing = False

        # Τρέχουσες τιμές
        self.name_label = Label(text="Όνομα: Αλβανός Δημήτριος")
        self.name_input = TextInput(text="Αλβανός Δημήτριος", multiline=False, size_hint_y=None, height=dp(40))

        self.email_label = Label(text="Email: mimis@example.com")
        self.email_input = TextInput(text="mimis@example.com", multiline=False, size_hint_y=None, height=dp(40))

        self.edit_btn = Button(text="Edit", size_hint_y=None, height=dp(44))
        self.edit_btn.bind(on_press=self.toggle_edit)

        self.build_static()

    def build_static(self):
        self.clear_widgets()
        self.add_widget(Label(text="[b]Προφίλ Χρήστη[/b]", markup=True, font_size=dp(22)))
        self.add_widget(self.name_label)
        self.add_widget(self.email_label)
        self.add_widget(self.edit_btn)

        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(40))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def toggle_edit(self, instance):
        if not self.editing:
            self.clear_widgets()
            self.add_widget(Label(text="[b]Προφίλ Χρήστη[/b]", markup=True, font_size=dp(22)))
            self.add_widget(self.name_input)
            self.add_widget(self.email_input)
            self.edit_btn.text = "Save"
            self.add_widget(self.edit_btn)

            back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(40))
            back_btn.bind(on_press=self.go_back)
            self.add_widget(back_btn)

        else:
            name = self.name_input.text
            email = self.email_input.text

            # Έλεγχος: μόνο ελληνικά στο όνομα
            if not re.fullmatch(r"[Α-Ωα-ωΆ-Ώά-ώ\s]+", name):
                self.show_error("[b]Το όνομα πρέπει να περιέχει μόνο ελληνικά.[/b]")
                return

            # Έλεγχος: όχι ελληνικά στο email
            if re.search(r"[Α-Ωα-ωΆ-Ώά-ώ]", email):
                self.show_error("[b]Το email δεν πρέπει να περιέχει ελληνικά.[/b]")
                return

            # Αν όλα ΟΚ, ενημέρωση και εμφάνιση
            self.name_label.text = f"Όνομα: {name}"
            self.email_label.text = f"Email: {email}"
            self.edit_btn.text = "Edit"

            self.clear_widgets()
            self.add_widget(Label(text="[b]Προφίλ Χρήστη[/b]", markup=True, font_size=dp(22)))
            self.add_widget(self.name_label)
            self.add_widget(self.email_label)
            self.add_widget(self.edit_btn)

            saved_label = Label(
                text="[b]Saved changes[/b]",
                markup=True,
                color=(0, 0.6, 0, 1),
                font_size=dp(14),
                size_hint_y=None,
                height=dp(30)
            )
            self.add_widget(saved_label)

            back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(40))
            back_btn.bind(on_press=self.go_back)
            self.add_widget(back_btn)

        self.editing = not self.editing

    def show_error(self, message):
        # Εμφάνιση μόνο μηνύματος λάθους, χωρίς clear για να μη χαθούν τα πεδία
        error_label = Label(
            text=message,
            markup=True,
            color=(1, 0, 0, 1),
            font_size=dp(14),
            size_hint_y=None,
            height=dp(30)
        )
        self.add_widget(error_label)

    def go_back(self, instance):
        self.screen_manager.current = 'home'
