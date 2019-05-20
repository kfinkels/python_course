from session2.classes.compressors.gzip_compressor import GzipCompressor
from session2.classes.compressors.rar_compressor import RarCompressor
from session2.classes.compressors.zip_compressor import ZipCompressor
from session2.classes.enums import CompressionType, TransferType


def supply(address, compression_type, transfer_type, transfer_params):
    local_path = download_file(address)
    compressed_local_path = compress_file(local_path, compression_type)
    transfer_file(compressed_local_path, transfer_type, transfer_params)


def download_file(address):
    print(f"Downloading from {address}")
    local_path = f"\\tmp\\{address.split('/')[-1]}"
    return local_path


def compress_file(path, type):
    if type == CompressionType.ZIP:
        return ZipCompressor(path).compress()
    elif type == CompressionType.GZIP:
        return GzipCompressor(path).compress()
    elif type == CompressionType.RAR:
        return RarCompressor(path).compress()


def transfer_file(path, type, transfer_params):
    if type == TransferType.FTP:
        print(f"Transferring {path} via FTP to {transfer_params['server']}:{transfer_params['port']}")
    if type == TransferType.SFTP:
        print(f"Transferring {path} via SFTP to {transfer_params['server']}:{transfer_params['port']}")
    if type == TransferType.S3:
        print(f"Transferring {path} via S3 to {transfer_params['address']}:{transfer_params['account_id']}")
    if type == TransferType.HTTP:
        print(f"Transferring {path} via HTTP to {transfer_params['address']}")


if __name__ == '__main__':
    supply(
        "s3://something/file.csv",
        CompressionType.ZIP,
        TransferType.FTP,
        dict(
            server="ftp://something",
            port=20
        )
    )
