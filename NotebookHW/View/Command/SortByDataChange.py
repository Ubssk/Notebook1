from NotebookHW.View.Command.Command import Command


class SortByDataChange(Command):

    def __init__(self, consoleUI):
        self.consoleUI = consoleUI
        super().__init__("Сортировать заметки по дате изменения",self.consoleUI)
    def execute(self) -> None:
        self.consoleUI.note_sort_by_data_change()