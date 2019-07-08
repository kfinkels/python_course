import zipfile

from session2.classes.compressors.base import CompressorBase


class ZipCompressor(CompressorBase):
    def compress(self, output_file_path):
        print(f"Compressing {output_file_path} to ZIP")

        output_file_path = output_file_path.replace(".csv", ".zip")
        output_file = zipfile.ZipFile(output_file_path, mode='w')
        output_file.write(output_file_path)
