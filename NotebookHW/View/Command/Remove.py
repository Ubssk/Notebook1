from NotebookHW.View.Command.Command import Command


class Remove(Command):

    def __init__(self, consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Удалить заметку",self.consoleUI)
    def execute(self) -> None:
        self.consoleUI.remove_note()