import sqlite3

connection = sqlite3.connect('Qanda.db')

cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE qanda (
        question text,
        answer text
    )
    """
)
connection.commit()

connection.close()