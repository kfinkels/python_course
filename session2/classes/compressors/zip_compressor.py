import zipfile

from session2.classes.compressors.base import CompressorBase


class ZipCompressor(CompressorBase):
    def __init__(self, output_path):
        output_file_path = output_path.replace(".csv", ".zip")
        self.output_file = zipfile.ZipFile(output_file_path, mode='w')

    def compress(self, file):
        print(f"Compressing {file} to ZIP")
        self.output_file.write(file)
