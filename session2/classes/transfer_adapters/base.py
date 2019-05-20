from abc import ABC, abstractmethod


class TransferAdapterBase(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def transfer(self):
        pass
