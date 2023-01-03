#!/usr/bin/env python3

import sqlite3

#creates the database if it doesn't exist
conn = sqlite3.connect('todo.db')

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        priority INTEGER NOT NULL
        );''')

# Creating tuples for the entry
tasks = [
        ('My first task', 1),
        ('My second task', 5),
        ('My third task', 10),
        ]

#Adding one entry
#c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('My first task', 1))

#Addin multiple entries
c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)

conn.commit()
conn.close()

