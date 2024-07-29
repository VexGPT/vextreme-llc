import sqlite3

conn = sqlite3.connect('Database/vex_gpt_source_of_truth.db')

c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS context (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    context TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Database setup completed.")