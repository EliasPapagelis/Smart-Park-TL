import sqlite3

def print_all_reservations():
    conn = sqlite3.connect("smartpark.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reservations")
    rows = cursor.fetchall()

    print("Όλες οι Κρατήσεις:")
    for row in rows:
        print(row)

    conn.close()

# Κάλεσέ το για δοκιμή
print_all_reservations()
