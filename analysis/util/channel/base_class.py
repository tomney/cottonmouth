import abc


class Channel(abc.ABC):

    @abc.abstractmethod
    def read(self, rows: int = -1):
        pass
