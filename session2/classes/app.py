from session2.classes.enums import CompressionType, TransferType


def supply(config):
    local_path = download_file(config["address"])
    compressed_local_path = compress_file(local_path, config[""])

def download_file(address):
    print(f"Downloading from {address}")


def compress_file(path, type):


if __name__ == '__main__':
    config = {
        "address": "s3://...",
        "compression_type": CompressionType.ZIP,
        "transfer_type": TransferType.FTP
    }

    supply(config)
