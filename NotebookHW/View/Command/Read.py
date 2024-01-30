from NotebookHW.View.Command.Command import Command


class Read(Command):

    def __init__(self, consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Востанить список заметок из сохранненого файла",self.consoleUI)
    def execute(self) -> None:
        self.consoleUI.read_note()