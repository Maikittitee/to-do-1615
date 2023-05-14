from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User import User


class System:
    def __init__(self):
        self.__users = []

    @property
    def users(self):
        return (self.__users)
    
    def add_user(self, new_user: "User"):
        self.__users.append(new_user)

    def register(self, new_user: "User"):
        for exist_user in self.users:
            if (new_user.username == exist_user.username):
                return (0)
        self.add_user(new_user)
        return (new_user)
    
    def login(self, username, password):
        for exist_user in self.users:
            if (exist_user.username == username):
                if (exist_user.password == password):
                    return (1)
        return (0)
                    

system = System()