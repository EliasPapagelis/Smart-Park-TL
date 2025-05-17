import sys
import os
from kivy.uix.label import Label

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))






# tests/test_app.py
import unittest
from kivy.base import EventLoop
from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')

# Φόρτωση Kivy πριν τις δοκιμές
EventLoop.ensure_window()

from app_screens.profile import ProfileScreen
from app_screens.reservation_info import ReservationInfoScreen
from app_screens.technical_support import TechnicalSupportScreen

class DummyScreenManager:
    def __init__(self):
        self.current = "home"

class TestSmartPark(unittest.TestCase):

    def setUp(self):
        self.sm = DummyScreenManager()

    def test_profile_edit_toggle(self):
        screen = ProfileScreen(self.sm)
        screen.toggle_edit(None)  # ενεργοποίηση edit
        screen.name_input.text = "Νέο Όνομα"
        screen.toggle_edit(None)  # αποθήκευση αλλαγών
        self.assertIn("Νέο Όνομα", screen.name_label.text)


    def test_reservation_cancel(self):
        screen = ReservationInfoScreen(self.sm)
        screen.cancel_reservation(None)
        self.assertTrue(any("Cancelled" in w.text for w in screen.children if isinstance(w, Label)))

    def test_technical_support_response(self):
        screen = TechnicalSupportScreen(self.sm)
        screen.message_input.text = "Χρειάζομαι βοήθεια"
        screen.send_message(None)
        last = screen.chat_box.children[0].text
        self.assertIn("Admin", last)

if __name__ == '__main__':
    unittest.main()
