from abc import ABC, abstractmethod


class CompressorBase(ABC):
    def __init__(self, output_path):
        self.output_path = output_path

    # @abstractmethod
    # def compress(self, path):
    #     pass

    def __repr__(self):
        print(f"path: {self.output_path}")

