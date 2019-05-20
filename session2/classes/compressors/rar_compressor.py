from session2.classes.compressors.base import CompressorBase


class RarCompressor(CompressorBase):
    def compress(self):
        print(f"Compressing {self.path} to Rar")
        return f"{self.path}.rar"
