import zipfile

from session2.classes.compressors.base import CompressorBase


class ZipCompressor(CompressorBase):
    def compress(self):
        print(f"Compressing {self.path} to ZIP")

        output_file_path = self.path.replace(".csv", ".zip")
        output_file = zipfile.ZipFile(output_file_path, mode='w')
        output_file.write(self.path)
