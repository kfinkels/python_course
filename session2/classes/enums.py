from enum import Enum, auto


class CompressionType(Enum):
    ZIP = auto(),
    GZIP = auto(),
    RAR = auto()


class TransferType(Enum):
    FTP = auto(),
    SFTP = auto(),
    S3 = auto(),
    HTTP = auto()
