import unittest
import sys
import os
import sqlite3  

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kivy.uix.screenmanager import ScreenManager  
from kivy.uix.label import Label

from app_screens.profile import ProfileScreen
from app_screens.reservation_info import ReservationInfoScreen
from app_screens.technical_support import TechnicalSupportScreen
from database import init_db, save_reservation, get_last_reservation


class TestSmartPark(unittest.TestCase):

    def setUp(self):
        init_db()
        self.sm = ScreenManager()

    def test_profile_edit_toggle(self):
        screen = ProfileScreen(self.sm)
        screen.toggle_edit(None)
        screen.name_input.text = "Νέο Όνομα"
        screen.toggle_edit(None)
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

    #def test_reservation_saved_to_database(self):
        #conn = sqlite3.connect("smartpark.db")
        #cursor = conn.cursor()
       # cursor.execute("SELECT * FROM reservations ORDER BY id DESC LIMIT 1")
        #result = cursor.fetchone()
       # conn.close()

       #self.assertIsNotNone(result, "Η βάση δεν περιέχει κρατήσεις.")
       # self.assertEqual(len(result), 5, "Η εγγραφή δεν έχει σωστά πεδία.")

if __name__ == '__main__':
    unittest.main()
