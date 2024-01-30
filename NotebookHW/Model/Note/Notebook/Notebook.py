from NotebookHW.Model.Note.Note.Note import Note


class Notebook:

    def __init__(self):
        self.notes = []

    def get_notes(self) -> list:
        return self.notes

    def set_notes(self, list):
        self.notes = list

    def dump(self):
        return {"Заметки": {"Заметка №": Note.get_note_id(), "Заголовок": Note.set_note_title(),
                            "Содержание": Note.set_note_body(),
                            "Дата создания": Note.get_note_data_creating_str(),
                            "Дата изменения": Note.get_note_data_change_str()}}

    def add_note(self, note):
        self.notes.append(note)

    def remove_note(self) -> None:
        list_note = self.get_notes()
        print("Номера заметок : ")
        for i in list_note:
            id_int = Note.get_note_id(i)
            print(id_int)
        try:
            number_note = int(input("Введите номер заметки, которую требуется удалить: "))
            flag = False
            for i in self.notes:
                if i.get_note_id() == number_note:
                    self.notes.remove(i)
                    flag = True
            if flag:
                print("Заметка успешно удалена!\n-----------------------\n")
            else:
                print("Заметки с таким номером нет в списке!\n-------------------\n")
        except Exception:
            print("Просьба число!")

    def change_note(self) -> None:
        list_note = self.get_notes()
        print("Номера заметок : ")
        for i in list_note:
            id_int = Note.get_note_id(i)
            print(id_int)
        try:
            number_note = int(input("Введите номер заметки, которую требуется изменить: "))
            flag = False
            for i in self.notes:
                if i.get_note_id() == number_note:
                    while (not flag):
                        op = int(
                            input("Заметка найдена, что вы хотите изменить Заголовок или Содержание. Нажмите 1 или 2: "))
                        if op == 1:
                            new_title = input("Введите новый заголовок: ")
                            i.set_note_title(new_title)
                            print("Заголовок заметки изменен")
                            flag = True
                        elif op == 2:
                            new_body = input("Введите новое содержание: ")
                            i.set_note_body(new_body)
                            print("Содержание заметки изменено")
                            flag = True
                        else:
                            print("Вы ввели не верную операцию, попробуйте еще раз!")

            if not flag: print("Заметки с таким номером не существует!\n------------------------------")
        except Exception:
            print("Введите число!")

    def print_note_by_id(self):
        note_id = None
        list_note = self.get_notes()
        print("Номера заметок : ")
        for i in list_note:
            id_int = Note.get_note_id(i)
            print(id_int)
        flag1 = True
        while (flag1):
            try:
                note_id = int(
                    input("Введите номер заметки из списка выше, которую хотите просмотреть:  "))
                flag1 = False
            except ValueError:
                print("Введите число!")

        flag = False
        for i in list_note:
            id_int = Note.get_note_id(i)
            if note_id == id_int:
                print(Note.note_to_string(i))
                flag = True

        if flag == False:
            print("Заметки с таким номером не сущесвует, попробуйте еще раз!")
            self.print_note_by_id()

    def sort_by_data_creating(self):
        list_sort_notes =sorted(self.get_notes(),key=lambda note:note.get_note_data_creating())
        self.set_notes(list_sort_notes)

    def sort_by_data_change(self):
        list_sort_notes = sorted(self.get_notes(), key=lambda note: note.get_note_data_change())
        self.set_notes(list_sort_notes)

    def to_string(self):
        for i in self.get_notes():
            print(i.note_to_string())