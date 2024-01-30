from NotebookHW.Model.FileHandler.FileHandler import FileHandler
from NotebookHW.Model.Note.Service import Service

class Presenter:
    def __init__(self, view):
        self.view = view
        self.service_note = Service(FileHandler())

    def add_note(self, title, body):
        self.service_note.add_note(title, body)

    def remove_note(self):
        self.service_note.remove_notes()

    def note_print_by_id(self):
        self.service_note.note_print_by_id()

    def all_print_note(self):
        self.service_note.to_string()

    def sort_note_by_data_creating(self):
        self.service_note.note_sort_by_data_creating()

    def sort_note_by_data_change(self):
        self.service_note.note_sort_by_data_change()

    def note_save(self):
        self.service_note.save()

    def note_read(self):
        self.service_note.read()

    def change_note(self):
        self.service_note.change_note()