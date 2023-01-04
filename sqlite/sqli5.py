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
        ('NAture Walk', 10),
        ]

c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)
conn.commit()

while True:
    try:
        name_1 = input("Enter task name: ")
    except ValueError:
        print("The name entered cannot be validated.")
        continue
    else:
        break
            
while True:
    try:
        priority_1 = int(input('Enter priority: '))
    except ValueError:
        print('The value entered is not an integer')
        continue
    else:
        break
c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name_1, priority_1))
conn.commit()

for row in c.execute('SELECT * FROM tasks'):
    print(row)

while True:
    try:
        priority_2 = int(input('Enter the priority: '))
    except ValueError:
        print('The value should be an integer')
        continue
    else:
        break

while True:
    try:
        id_update = int(input('Enter the id of the task to be editted: '))
    except ValueError:
        print('The value should be an integer')
        continue
    else:
        break

c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (priority_2, id_update))
conn.commit()

conn.close()
