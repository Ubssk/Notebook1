from NotebookHW.View.Command.Add import Add
from NotebookHW.View.Command.Print import Print
from NotebookHW.View.Command.Change import Change
from NotebookHW.View.Command.Finish import Finish

from NotebookHW.View.Command.PrintById import PrintById
from NotebookHW.View.Command.SortByDataChange import SortByDataChange
from NotebookHW.View.Command.SortByDataCreating import SortByDataCreating
from NotebookHW.View.Command.Read import Read
from NotebookHW.View.Command.Remove import Remove
from NotebookHW.View.Command.Save import Save

class MainMenu:

    def __init__(self,consoleUI):
        self.command = []
        self.command.append(Add(consoleUI))
        self.command.append(Change(consoleUI))
        self.command.append(Remove(consoleUI))
        self.command.append(PrintById(consoleUI))
        self.command.append(SortByDataCreating(consoleUI))
        self.command.append(SortByDataChange(consoleUI))
        self.command.append(Print(consoleUI))
        self.command.append(Read(consoleUI))
        self.command.append(Save(consoleUI))
        self.command.append(Finish(consoleUI))

    def menu(self):
        st = ""
        for i in range(len(self.command)):
            st = str(st) + str(i+1) + " " + self.command[i].get_discription() + "\n"

        return st


    def execute(self, choice) -> None:
        commands = self.command[choice - 1]
        commands.execute()

    def size(self) -> int:
        return len(self.command)