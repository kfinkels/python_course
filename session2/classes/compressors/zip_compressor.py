from session2.classes.compressors.base import CompressorBase


class ZipCompressor(CompressorBase):
    def compress(self):
        print(f"Compressing {self.path} to ZIP")
        return f"{self.path}.zip"
