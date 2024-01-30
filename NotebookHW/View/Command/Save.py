from NotebookHW.View.Command.Command import Command

class Save(Command):

    def __init__(self, consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Сохранить список заметок",self.consoleUI)

    def execute(self) -> None:
        self.consoleUI.note_save()