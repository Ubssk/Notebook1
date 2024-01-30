from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, discription,consoleUI):
        self.discription = discription
        self.consoleUI = consoleUI


    def get_discription(self)-> str:
        return self.discription

    def get_consoleUI(self):
        return self.consoleUI

    @abstractmethod
    def execute(self) -> None:
        pass