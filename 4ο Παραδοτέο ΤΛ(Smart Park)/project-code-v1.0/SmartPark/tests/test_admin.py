import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kivy.uix.screenmanager import ScreenManager
from admin_apps_screens.tech_supp import AdminTechSupportScreen
from admin_apps_screens.offers import OffersScreen
from admin_apps_screens.edit_hours import EditHoursScreen
from database import init_db, save_support_message, load_support_messages


class TestAdminFunctions(unittest.TestCase):

    def setUp(self):
        init_db()
        self.sm = ScreenManager()

    def test_admin_sends_support_message(self):
        screen = AdminTechSupportScreen(self.sm)
        screen.message_input.text = "Μήνυμα από admin"
        screen.send_message(None)

        # Έλεγχος αν αποθηκεύτηκε το μήνυμα του admin
        messages = load_support_messages()
        self.assertTrue(any(m[0] == 'admin' and m[1] == "Μήνυμα από admin" for m in messages))

    def test_add_offer_text(self):
        screen = OffersScreen(self.sm)
        screen.parking_spinner.values = ("Parking A",)
        screen.parking_spinner.text = "Parking A"
        screen.offer_input.text = "30% έκπτωση"
        screen.add_offer(None)

        # Το προσθέτει στο offers dict
        self.assertEqual(screen.offers_data["Parking A"], ["30% έκπτωση"])


    def test_edit_hours_fields_exist(self):
        screen = EditHoursScreen(self.sm)
        self.assertTrue(hasattr(screen, "start_time"))
        self.assertTrue(hasattr(screen, "end_time"))

    
if __name__ == '__main__':
    unittest.main()
