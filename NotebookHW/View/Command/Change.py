from NotebookHW.View.Command.Command import Command


class Change(Command):

    def __init__(self, consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Изменить заметку", self.consoleUI)

    def execute(self) -> None:
        self.consoleUI.change_note()