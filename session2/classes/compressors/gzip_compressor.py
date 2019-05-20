from session2.classes.compressors.base import CompressorBase


class GzipCompressor(CompressorBase):
    def compress(self):
        print(f"Compressing {self.path} to GZIP")
        return f"{self.path}.gzip"
