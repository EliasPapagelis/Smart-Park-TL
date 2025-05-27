import sqlite3
from datetime import datetime
import random

def init_db():
    conn = sqlite3.connect("smartpark.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS support_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')



    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            parking TEXT NOT NULL,
            spot TEXT NOT NULL,
            date_from TEXT NOT NULL,
            date_to TEXT NOT NULL
             
        )
    ''')

    cursor.execute("PRAGMA table_info(reservations)")
    columns = [row[1] for row in cursor.fetchall()]

    # Αν δεν υπάρχει το status, πρόσθεσέ το
    if 'status' not in columns:
        cursor.execute('''
            ALTER TABLE reservations
            ADD COLUMN status TEXT DEFAULT 'pending'
        ''')


    # Έλεγχος για ύπαρξη πεδίου sender (αν τρέχεις σε παλιά βάση)
    cursor.execute("PRAGMA table_info(support_messages)")
    columns = [col[1] for col in cursor.fetchall()]
    if 'sender' not in columns:
        cursor.execute("ALTER TABLE support_messages ADD COLUMN sender TEXT DEFAULT 'user'")

    conn.commit()
    conn.close()

def save_support_message(message, sender='user'):
    conn = sqlite3.connect("smartpark.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO support_messages (sender, message, timestamp)
        VALUES (?, ?, ?)
    ''', (sender, message, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def load_support_messages():
    conn = sqlite3.connect("smartpark.db")
    cursor = conn.cursor()
    cursor.execute("SELECT sender, message, timestamp FROM support_messages ORDER BY id ASC")
    messages = cursor.fetchall()
    conn.close()
    return messages


def is_spot_available(parking, spot, date_from, date_to):
    conn = sqlite3.connect("smartpark.db")
    c = conn.cursor()
    c.execute('''
        SELECT * FROM reservations
        WHERE parking=? AND spot=? AND (
            (date_from <= ? AND date_to >= ?) OR
            (date_from <= ? AND date_to >= ?) OR
            (date_from >= ? AND date_to <= ?)
        )
    ''', (parking, spot, date_from, date_from, date_to, date_to, date_from, date_to))
    result = c.fetchall()
    conn.close()
    return len(result) == 0  # True = διαθέσιμη


def save_reservation(parking, spot, date_from, date_to):
    conn = sqlite3.connect("smartpark.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO reservations (parking, spot, date_from, date_to)
        VALUES (?, ?, ?, ?)
    ''', (parking, spot, date_from, date_to))
    conn.commit()
    conn.close()




def get_last_reservation():
    conn = sqlite3.connect("smartpark.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result


def delete_last_reservation():
    conn = sqlite3.connect("smartpark.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id = (SELECT id FROM reservations ORDER BY id DESC LIMIT 1)")
    conn.commit()
    conn.close()

def get_fine_amount(reservation_id):
    # Για παράδειγμα, επιστρέφουμε τυχαίο πρόστιμο μεταξύ 10€ και 100€
    return random.randint(10, 100)



def mark_fine_paid(reservation_id):
    conn = sqlite3.connect("smartpark.db")
    cursor = conn.cursor()
    # Εδώ θα μπορούσες π.χ. να ενημερώσεις ένα πεδίο status, 
    # ή να καταχωρήσεις σε πίνακα payments. Για demo:
    cursor.execute("""
        UPDATE reservations 
        SET status = 'paid'
        WHERE id = ?
    """, (reservation_id,))
    conn.commit()
    conn.close()


