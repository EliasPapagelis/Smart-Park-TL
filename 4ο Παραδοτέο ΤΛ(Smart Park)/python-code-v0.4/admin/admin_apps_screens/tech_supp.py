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






class AdminTechSupportScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text="Admin Technical Support Page (υπό κατασκευή)"))

