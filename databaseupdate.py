import sqlite3

connection = sqlite3.connect('Qanda.db')

cursor = connection.cursor()

cursor.execute(
    """
    INSERT INTO qanda VALUES(
        'What is Python',"Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together."
    )
    """
)
connection.commit()

connection.close()