import sqlite3

# Connect (creates database file if not exists)
conn = sqlite3.connect('site.db')

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS USERS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

# Save changes
conn.commit()

# Close connection
conn.close()

# def get_db():
#     conn = sqlite3.connect("site.db")
#     conn.row_factory = sqlite3.Row
#     return conn
