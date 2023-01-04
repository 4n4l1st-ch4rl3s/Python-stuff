#!/usr/bin/env python
import sqlite3
import string

class make_db:
    #create database
    def __init__(self):
        self.conn = sqlite3.connect('sqlite5.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            priority TEXT NOT NULL,
            );''')

    #add task
    def add_task(self):
        tasks = [
        ('Hacking', 1),
        ('Swimming', 5),
        ('Reading',2),
        ('Nature Walk', 10),
        ('Jogging', 15),
        ]

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)
        self.conn.commit()

    #manually add task
    def add_manual_tasks(self):
        while True:
            name  = input('Name of the task: ')
            invalidcharacters= set(string.punctuation)
            if any(char in invalidcharacters for char in name):
                print('Invalid characters in name')
                continue
            else:
                break
            
        while True:
            priority = input('Priority of the task: ')
            try:
                priority = int(priority)
            except ValueError:
                print('Invalid priority')
                continue
            else:
                break

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))

        self.conn.commit()

    #show tasks in database
    def show_tasks(self):        
        for row in self.c.execute('SELECT * FROM tasks'):
            print(row)

    #update priority of a task
    def update_tasks(self):
        priority = input('Priority of the task: ')
        try:
            priority = int(priority)
        except ValueError:
            print('Invalid priority')
            return

        number = input('Id number of the task: ')
        try:
            number = int(number)
        except ValueError:
            print('Invalid id number')
            return

        self.c.execute('UPDATE tasks SET priority =? WHERE id =?', (priority,number))

    #delete task
    def delete_task(self):
        number  = input('Number of tasks to delete: ')
        try:
            number = int(number)
        except ValueError:
            print('Invalid number')
            return
        self.c.execute('DELETE FROM tasks WHERE id=?', (number,))
        self.conn.commit()        


# calls function to create our database
app = make_db()
#add our task to the database
app.add_task()
#you can add more tasks to the database using the app.add_manual() function

#you can list tasks using the app.list_tasks() function

#you can update tasks using the app.update_tasks()

#you can delete tasks using the app.delete_task()

app.conn.close()