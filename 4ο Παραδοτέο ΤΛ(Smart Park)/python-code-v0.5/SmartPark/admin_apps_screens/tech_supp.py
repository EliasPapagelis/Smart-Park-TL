

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import dp

from database import load_support_messages, save_support_message

class AdminTechSupportScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager

        self.add_widget(Label(text="[b]Admin Technical Support[/b]", markup=True, font_size=dp(22)))

        self.chat_area = ScrollView(size_hint=(1, 0.8))
        self.chat_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=dp(5))
        self.chat_box.bind(minimum_height=self.chat_box.setter('height'))
        self.chat_area.add_widget(self.chat_box)
        self.add_widget(self.chat_area)

        # Φόρτωση όλων των μηνυμάτων
        self.load_messages()

        self.message_input = TextInput(
            size_hint_y=None, height=dp(40),
            multiline=False, hint_text="Γράψτε την απάντησή σας..."
        )
        self.add_widget(self.message_input)

        send_btn = Button(text="Αποστολή", size_hint_y=None, height=dp(50))
        send_btn.bind(on_press=self.send_message)
        self.add_widget(send_btn)

        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(40))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def load_messages(self):
        self.chat_box.clear_widgets()
        for sender, msg, timestamp in load_support_messages():
            prefix = "[b]Εσύ:[/b]" if sender == 'admin' else "[b]Χρήστης:[/b]"
            label = Label(
                text=f"{prefix} {msg}\n[i]{timestamp.split('T')[0]} {timestamp.split('T')[1][:8]}[/i]",
                markup=True, font_size=dp(14), size_hint_y=None, height=dp(60)
            )
            self.chat_box.add_widget(label)
        self.chat_area.scroll_y = 0

    def send_message(self, instance):
        msg = self.message_input.text.strip()
        if msg:
            save_support_message(msg, sender='admin')
            self.message_input.text = ''
            self.load_messages()

    def go_back(self, instance):
        self.screen_manager.current = 'admin_home'
