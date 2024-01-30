from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def save(self, o):
        pass

    @abstractmethod
    def read(self, file_path) -> list:
        pass
