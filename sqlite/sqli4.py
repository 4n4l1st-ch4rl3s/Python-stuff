#!/usr/bin/env python3

import sqlite3

class find_task:
    def __init__(self):
        self.conn = sqlite3.connect('todo4.db')
        self.c = self.conn.cursor()
        self.create_task_table()
        
    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            priority INTEGER NOT NULL
            );''')
            
    def add_task(self):
        while True:
            try:
                name = input("Enter task name: ")
            except ValueError:
                print("The name entered cannot be validated.")
                continue
            else:
                break
            
        while True:
            try:
                priority = int(input('Enter priority: '))
            except ValueError:
                print('The value entered is not an integer')
                continue
            else:
                break
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()

app = find_task()
app.add_task()

app.c.execute('SELECT * FROM tasks')
rows = app.c.fetchall()

for row in rows:
    print(row)
app.conn.close()
