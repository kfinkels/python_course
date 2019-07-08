from enum import Enum, auto


class CompressionType(Enum):
    ZIP = "compressors.zip_compressor.ZipCompressor"
    GZIP = "compressors.gzip_compressor.GzipCompressor"
    RAR = "compressors.rar_compressor.RarCompressor"


class TransferType(Enum):
    FTP = auto(),
    SFTP = auto(),
    S3 = auto(),
    HTTP = auto()
