from System import system
from datetime import datetime
from Task import Task

class   User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__todo_list = [] # composition ToDo

    @property
    def username(self):
        return (self.__username)
    
    @property 
    def password(self):
        return (self.__password)

    @staticmethod
    def register(username, password):
        new_user = User(username, password)
        return (system.register(new_user))
    
    @staticmethod
    def login(username, password):
        return (system.login(username, password))
    
    def get_todo_by_date(date:datetime):
        for to

    def add_new_task(self, date:datetime, task:Task):
        self.



res = User.register("Maiki","1234")
res2 = User.register("Maikiddd","12224")
print(res)
print(res2)

print("login")

print(User.login("Maiki","1234"))