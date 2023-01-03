#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('todo3.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            priority INTEGER NOT NULL
            );''')

tasks = [
        ('Hacking', 1),
        ('Swimming', 5),
        ('Reading',2),
        ]

c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)
conn.commit()

for row in c.execute('SELECT * FROM tasks'):
    print(row)
conn.close()
