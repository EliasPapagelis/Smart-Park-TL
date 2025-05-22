# payment_screen.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp
from database import get_last_reservation, get_fine_amount, mark_fine_paid

class PaymentScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)
        self.screen_manager = screen_manager

        self.add_widget(Label(text="[b]Πληρωμή Προστιμού[/b]", markup=True, font_size=dp(22)))

        # Παίρνουμε την τελευταία κράτηση από τη βάση
        reservation = get_last_reservation()
        if reservation:
            res_id, parking, spot, start, end, status = reservation

            # Ποσό προστίμου
            amount = get_fine_amount(res_id)
            self.res_id = res_id

            self.add_widget(Label(
                text=f"Reservation ID: {res_id}\nParking: {parking}\nSpot: {spot}",
                font_size=dp(16)
            ))
            self.add_widget(Label(
                text=f"[b]Ποσό Προστίμου:[/b] {amount}€",
                markup=True, font_size=dp(18), color=(1, 0, 0, 1)
            ))

            pay_btn = Button(
                text="Έγκριση πληρωμής",
                size_hint_y=None, height=dp(50),
                background_color=(0.1, 0.7, 0.3, 1), color=(1,1,1,1)
            )
            pay_btn.bind(on_press=self.do_payment)
            self.add_widget(pay_btn)

        else:
            self.add_widget(Label(text="Δεν βρέθηκε ενεργή κράτηση.", font_size=dp(16)))

        back_btn = Button(text="Πίσω", size_hint_y=None, height=dp(40))
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)

    def do_payment(self, instance):
        # Σηματοδοτούμε στο DB ότι το πρόστιμο πληρώθηκε
        mark_fine_paid(self.res_id)
        self.clear_widgets()
        self.add_widget(Label(
            text="[b]Η πληρωμή ολοκληρώθηκε με επιτυχία![/b]",
            markup=True, font_size=dp(18), color=(0,0.6,0,1)
        ))
        done_btn = Button(text="Τέλος", size_hint_y=None, height=dp(44))
        done_btn.bind(on_press=self.go_back)
        self.add_widget(done_btn)

    def go_back(self, instance):
        self.screen_manager.current = 'reservation_info'
