import sqlite3
from datetime import datetime

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
    conn.commit()
    conn.close()

def save_support_message(message):
    conn = sqlite3.connect("smartpark.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO support_messages (message, timestamp)
        VALUES (?, ?)
    ''', (message, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def load_support_messages():
    conn = sqlite3.connect("smartpark.db")
    cursor = conn.cursor()
    cursor.execute("SELECT message, timestamp FROM support_messages ORDER BY id ASC")
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


