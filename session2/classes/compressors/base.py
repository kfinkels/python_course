class CompressorBase:
    def __init__(self, path):
        self.path = path

    def compress(self):
        pass

    def __repr__(self):
        print(f"path: {self.path}")

