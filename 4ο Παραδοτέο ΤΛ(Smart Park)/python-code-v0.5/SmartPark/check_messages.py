import sqlite3

conn = sqlite3.connect("smartpark.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM support_messages")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Μήνυμα: {row[1]}, Ώρα: {row[2]}")

conn.close()
