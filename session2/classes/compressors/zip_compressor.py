import zipfile

from session2.classes.compressors.base import CompressorBase


class ZipCompressor(CompressorBase):
    def __init__(self, output_path):
        self.output_file = zipfile.ZipFile(output_path, mode='w')

    def compress(self, path):
        print(f"Compressing {path} to ZIP")
        self.output_file.write(path)
