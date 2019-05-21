import zipfile

from session2.classes.compressors.base import CompressorBase


class ZipCompressor(CompressorBase):
    def __init__(self, output_path):
        self.output_path = output_path
        self.output_file = None

    def compress(self, path):
        print(f"Compressing {path} to ZIP")
        self.output_file.write(path)

    def __enter__(self):
        self.output_file = zipfile.ZipFile(self.output_path, mode='w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.output_file.close()
