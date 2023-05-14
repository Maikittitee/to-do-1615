from enum import Enum

class   TaskImportant(Enum):
    IMPORTANT = 0
    NONIMPORTANT = 1
    URGENT = 2
    NONURGENT = 3

class TaskStatus(Enum):
    TODO = 0
    IN_PROGRESS = 1
    COMPLETE = 2


class   Task:
    def __init__ (self, topic, description, important:TaskImportant ,status:TaskStatus):
        self.__topic = topic
        self.__description = description
        self.__important = important
        self.__status = status