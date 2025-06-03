from abc import ABC, abstractmethod

class FileProcess(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass