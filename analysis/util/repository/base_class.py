from abc import ABC, abstractmethod

class Repository(abstractmethod):

    @abstractmethod
    def write():
        pass