import sqlite3

def clear_database():
    conn = sqlite3.connect("smartpark.db")
    cursor = conn.cursor()

    # Διαγραφή όλων των εγγραφών από κάθε πίνακα
    cursor.execute("DELETE FROM support_messages")
    cursor.execute("DELETE FROM reservations")

    conn.commit()
    conn.close()
    print("Η βάση καθαρίστηκε επιτυχώς.")

clear_database()
