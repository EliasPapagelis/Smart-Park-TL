from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.metrics import dp

class ReservationScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        
        #  background 
        with self.canvas.before:
            Color(1, 1, 1, 1)  
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        # Logo 
        logo = Label(
            text="[b]SMART PARK[/b]", 
            font_size=dp(24), 
            markup=True, 
            size_hint_y=None, 
            height=dp(50))
        logo.color = (0, 0, 0)  
        self.add_widget(logo)
        
        # Rent a spot Button 
        self.rent_btn = Button(
            text='Rent a spot',
            size_hint_y=None,
            height=dp(50),
            background_normal='',
            background_color=(0.68, 0.85, 0.9, 1),  
            color=(0, 0, 0, 1))  
        self.add_widget(self.rent_btn)
        
        # Reservation Info Button 
        self.res_info_btn = Button(
            text='Reservation Info',
            size_hint_y=None,
            height=dp(50),
            background_normal='',
            background_color=(0.68, 0.85, 0.9, 1),  
            color=(0, 0, 0, 1))  
        self.add_widget(self.res_info_btn)
        
        # Technical Support Button
        self.tech_support_btn = Button(
            text='Technical Support',
            size_hint_y=None,
            height=dp(50),
            background_normal='',
            background_color=(0.68, 0.85, 0.9, 1),  
            color=(0, 0, 0, 1))  
        self.add_widget(self.tech_support_btn)
        
       
        self.add_widget(Widget(size_hint_y=None, height=dp(20)))
        
        # MAKE RESERVATION Button 
        self.make_reservation_btn = Button(
            text='MAKE RESERVATION',
            size_hint_y=None,
            height=dp(60),
            background_normal='',
            background_color=(0.68, 0.85, 0.9, 1), 
            color=(1, 1, 1, 1),  
            bold=True,
            font_size=dp(18))
        self.add_widget(self.make_reservation_btn)
        
        
        self.add_widget(Widget(size_hint_y=None, height=dp(20)))
        
        # Tagline 
        tagline = Label(
            text="Easy, fast and smart way to park your vehicle", 
            font_size=dp(14),
            size_hint_y=None,
            height=dp(30))
        tagline.color = (0, 0, 0)  
        self.add_widget(tagline)
    
    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

class SmartParkApp(App):
    def build(self):
        Window.size = (360, 640) 
        return ReservationScreen()

if __name__ == "__main__":
    SmartParkApp().run()

