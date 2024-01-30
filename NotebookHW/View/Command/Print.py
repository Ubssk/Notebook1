from NotebookHW.View.Command.Command import Command


class Print(Command):

    def __init__(self,consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Вывести на экран все заметки",self.consoleUI)

    def execute(self) -> None:
        self.consoleUI.all_print_note()