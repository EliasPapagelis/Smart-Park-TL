import unittest
import sys
import os
import sqlite3  

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kivy.uix.screenmanager import ScreenManager  
from kivy.uix.label import Label
from datetime import datetime

from app_screens.profile import ProfileScreen
from app_screens.reservation_info import ReservationInfoScreen
from app_screens.technical_support import TechnicalSupportScreen
from database import init_db, save_reservation, get_last_reservation, mark_fine_paid

DB_PATH = "smartpark.db"

class TestSmartPark(unittest.TestCase):

    def setUp(self):
        init_db()
        self.sm = ScreenManager()
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

        # Καθάρισε τη βάση πριν από κάθε test
        self.cursor.execute("DELETE FROM reservations")
        self.conn.commit()

        
    def tearDown(self):
        self.conn.close()

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
        self.assertIn("Εσύ", last)


    def test_create_reservation(self):
        # Δεδομένα κράτησης
        parking = "Parking A"
        spot = "Θέση 1"
        date_from = "8:00"
        date_to = "14:00"

        # Αποθήκευση κράτησης
        save_reservation(parking, spot, date_from, date_to)

        # Έλεγχος αν υπάρχει στη βάση
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reservations")
        rows = cursor.fetchall()
        conn.close()

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], parking)
        self.assertEqual(rows[0][2], spot)
        self.assertEqual(rows[0][3], date_from)
        self.assertEqual(rows[0][4], date_to)



    def test_pay_fine_updates_status(self):
        # Δημιουργία κράτησης
        save_reservation("Parking A", "Θέση 1", "08:00", "10:00")

        # Πάρε το ID της τελευταίας κράτησης
        self.cursor.execute("SELECT id FROM reservations ORDER BY id DESC LIMIT 1")
        reservation_id = self.cursor.fetchone()[0]

        # Πλήρωσε το πρόστιμο
        mark_fine_paid(reservation_id)

        # Έλεγχος αν ενημερώθηκε το status
        self.cursor.execute("SELECT status FROM reservations WHERE id = ?", (reservation_id,))
        status = self.cursor.fetchone()[0]

        self.assertEqual(status, "paid")

    

if __name__ == '__main__':
    unittest.main()
