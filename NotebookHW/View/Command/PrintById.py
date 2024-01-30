from NotebookHW.View.Command.Command import Command


class PrintById(Command):

    def __init__(self, consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Вывести на экран заметку по номеру", self.consoleUI)

    def execute(self) -> None:
        self.consoleUI.note_print_by_id()