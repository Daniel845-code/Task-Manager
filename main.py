from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import sqlite3

class MainFrame(ScreenManager):
    pass

class Database():
    def recovery_tasks():
        #zone of database query code
        connection = sqlite3.connect('app.db')
        con = connection.cursor()
        query_result = con.execute('select title from tasks').fetchall()
        #end of zone
        return query_result

    def insert_task(tasks):
        connection = sqlite3.connect('app.db')
        con = connection.cursor()
        con.execute('insert into tasks (title) values ('+'"'+tasks+'"'+');')
        connection.commit()
        print(con.execute('select * from tasks').fetchall())

    def delete_task(task_title):
        connection = sqlite3.connect('app.db')
        con = connection.cursor()
        con.execute("delete from tasks where title="+"'"+task_title+"'")
        connection.commit()
        print(con.execute('select * from tasks').fetchall())

class Tasks(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

    def delete_task(self,task_title):
        task_title = self.ids.label.text
        Database.delete_task(task_title)


class Box(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        tasks = Database.recovery_tasks()
        for task in tasks:
            data = ''
            for letter in task:
                if (letter == '('):
                    pass
                elif (letter == ')'):
                    pass
                elif (letter == "'"):
                    pass
                elif (letter == "'"):
                    pass
                elif (letter == ','):
                    pass
                else:
                    data += letter
            else:
                self.add_widget(Tasks(text=data))

class TaskPanel(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def addWidget(self,text=''):
        text_input = self.ids.text_input.text
        Database.insert_task(text_input)
        self.ids.task.add_widget(Tasks(text=text_input))
        self.ids.text_input.text = ''


class Task(App):
    def build(self):
        return MainFrame()

Task().run()
