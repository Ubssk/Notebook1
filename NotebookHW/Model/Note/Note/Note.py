import datetime


class Note:
    id = 1
    def __init__(self, title, body):
        self.id = Note.id
        self.__title = title
        self.__body = body
        self.data_creation = datetime.datetime.now()
        self.data_change = datetime.datetime.now()
        Note.id += 1

    def dump(self) -> dict:
        dt_note = {"Заметка №": self.id, "Заголовок": self.__title, "Содержание": self.__body,
                   "Дата создания": self.data_creation.strftime("%Y/%m/%d  %H-%M-%S"),
                   "Дата изменения": self.data_change.strftime("%Y/%m/%d  %H-%M-%S")}
        return dt_note

    def get_note_id(self) -> int:
        return self.id

    def get_note_title(self) -> str:
        return self.__title

    def get_note_body(self) -> str:
        return self.__body

    def get_note_data_creating(self) -> datetime:
        return self.data_creation

    def get_note_data_creating_str(self) -> str:
        data_creating_str = self.data_creation.strftime("%Y/%m/%d  %H-%M-%S")
        return data_creating_str

    def get_note_data_change_str(self) -> str:
        data_change_str = self.data_change.strftime("%Y/%m/%d  %H-%M-%S")
        return data_change_str
    def set_note_data_creating(self,datatime):
        self.data_creation = datetime.datetime.replace(datatime)

    def set_note_data_change(self,datatime):
        self.data_change = datetime.datetime.replace(datatime)

    def get_note_data_change(self) -> datetime:
        return self.data_change

    def set_note_title(self, title) -> None:
        self.__title = title
        self.data_change = datetime.datetime.now()

    def set_note_body(self, body):
        self.__body = body
        self.data_change = datetime.datetime.now()

    def set_note_id(self,id):
        self.id = id

    def note_to_string(self):
        data1 = self.get_note_data_creating_str()
        data2 = self.get_note_data_change_str()
        return (f"Заметка №{self.id}\n\nЗаголовок - {self.__title}\n\nСодержание - {self.__body}"
                f"\n\nДата создания  :   {data1}"
                f"\nДата изменения :   {data2}\n"
                f"--------------------------------\n")