from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import json

class Tasks(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Box(BoxLayout):
    pass

class TaskPanel(Screen):
    tasks = []
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.loadData()
        for task in self.tasks:
            self.ids.task.add_widget(Tasks(text=task))

    def addWidget(self):
        text_input = self.ids.text_input.text
        self.ids.task.add_widget(Tasks(text=text_input))
        self.ids.text_input.text = ''
        self.tasks.append(text_input)
        self.saveData()

    def saveData(self,*kwargs):
        data = open('file.json','w')
        json.dump(self.tasks,data)

    def loadData(self,*kwargs):
        try:
            data = open('file.json','r')
            self.tasks = json.load(data)
        except:
            pass
            
    def RemoveWidget(self,task):
        text = task.ids.label.text
        self.ids.task.remove_widget(task)
        self.tasks.remove(text)
        self.saveData()

class Task(App):
    def build(self):
        return TaskPanel()

Task().run()
