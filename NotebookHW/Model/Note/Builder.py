from NotebookHW.Model.Note.Note.Note import Note

class Builder:
    def note_build(self, title, body) -> Note:
        note = Note(title, body)
        return note