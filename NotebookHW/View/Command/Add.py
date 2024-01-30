from NotebookHW.View.Command.Command import Command


class Add(Command):

    def __init__(self,consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Добавить заметку", consoleUI=self.consoleUI)


    def execute(self) -> None:
        self.consoleUI.add_note()