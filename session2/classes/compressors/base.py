from abc import ABC, abstractmethod


class CompressorBase(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def compress(self):
        pass

    def __repr__(self):
        print(f"path: {self.path}")

