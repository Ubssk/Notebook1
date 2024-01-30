import json

from NotebookHW.Model.Interface.Interface import Interface


class FileHandler(Interface):
    def save(self, my_list):
        with open("../../../data_file.json", "w", encoding="utf-8") as write_file:
            json.dump([o.dump() for o in my_list], write_file, ensure_ascii=False)

    def read(self) -> list:
        with open("../../../data_file.json", "r", encoding="utf-8") as read_file:
            my_list = [item for item in json.load(read_file)]
            return my_list
