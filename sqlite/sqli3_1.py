#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('todo3.db')

c = conn.cursor()

c.execute('SELECT * FROM tasks')

# This is not a good practice since if the database is large it may cause memory issues
rows = c.fetchall()

for row in rows:
    print(row)
conn.close()
