from session2.classes.compressors.gzip_compressor import GzipCompressor
from session2.classes.compressors.rar_compressor import RarCompressor
from session2.classes.compressors.zip_compressor import ZipCompressor
from session2.classes.enums import CompressionType, TransferType
from session2.classes.transfer_adapters.ftp_adapter import FTPAdapter
from session2.classes.transfer_adapters.s3_adapter import S3Adapter


class Supplier:
    def __init__(self, address, compression_type, transfer_type, transfer_params):
        self.address = address
        self.compression_type = compression_type
        self.transfer_type = transfer_type
        self.transfer_params = transfer_params

    def supply(self):
        local_path = self.__download_file()
        compressed_local_path = self.__compress_file(local_path)
        self.__transfer_file(compressed_local_path)

    def __download_file(self):
        print(f"Downloading from {self.address}")
        local_path = f"\\tmp\\{self.address.split('/')[-1]}"
        return local_path

    def __compress_file(self, path):
        if self.compression_type == CompressionType.ZIP:
            return ZipCompressor(path).compress()
        elif self.compression_type == CompressionType.GZIP:
            return GzipCompressor(path).compress()
        elif self.compression_type == CompressionType.RAR:
            return RarCompressor(path).compress()

    def __transfer_file(self, path):
        if self.transfer_type == TransferType.FTP:
            FTPAdapter(path, **self.transfer_params).transfer()
        if self.transfer_type == TransferType.S3:
            S3Adapter(path, **self.transfer_params).transfer()


if __name__ == '__main__':
    supplier = Supplier(
        address="s3://something/file.csv",
        compression_type=CompressionType.ZIP,
        transfer_type=TransferType.FTP,
        transfer_params=dict(
            server="ftp://something",
            port=20
        )
    )

    supplier.supply()
