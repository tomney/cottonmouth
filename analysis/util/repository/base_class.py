from abc import ABC, abstractmethod


class Repository(ABC):

    @abstractmethod
    def write(self):
        pass
