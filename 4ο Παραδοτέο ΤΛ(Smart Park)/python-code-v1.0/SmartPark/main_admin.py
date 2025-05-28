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
from admin_apps_screens.edit_hours import EditHoursScreen
from admin_apps_screens.home_screen import AdminHomeScreen
from admin_apps_screens.offers import OffersScreen
from admin_apps_screens.show_incomes import IncomesScreen
from admin_apps_screens.tech_supp import AdminTechSupportScreen
from database import init_db

# ---------- Κύρια εφαρμογή ----------
class AdminApp(App):
    def build(self):
        Window.size = (360, 640)
        sm = ScreenManager()

        # Αρχική admin σελίδα
        home_screen = Screen(name='admin_home')
        home_screen.add_widget(AdminHomeScreen(sm))
        sm.add_widget(home_screen)

        # Dummy οθόνες
        incomes_screen = Screen(name='incomes')
        incomes_screen.add_widget(IncomesScreen(sm))
        sm.add_widget(incomes_screen)

        edit_hours_screen = Screen(name='edit_hours')
        edit_hours_screen.add_widget(EditHoursScreen(sm))
        sm.add_widget(edit_hours_screen)

        offers_screen = Screen(name='offers')
        offers_screen.add_widget(OffersScreen(sm))
        sm.add_widget(offers_screen)

        tech_support_screen = Screen(name='tech_support')
        tech_support_screen.add_widget(AdminTechSupportScreen(sm))
        sm.add_widget(tech_support_screen)

        return sm


if __name__ == '__main__':
    init_db()
    AdminApp().run()
