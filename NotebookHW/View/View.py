from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def print_answer(self, answer) -> None:
        pass