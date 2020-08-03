import sqlite3

connection = sqlite3.connect('Qanda.db')

cursor = connection.cursor()

cursor.execute(
    """
    SELECT * FROM qanda
    """
)
print(cursor.fetchall())

connection.close()