from session2.classes.transfer_adapters.base import TransferAdapterBase


class S3Adapter(TransferAdapterBase):
    def __init__(self, path, address, access_key):
        super(S3Adapter, self).__init__(path)
        self.address = address
        self.access_key = access_key

    def transfer(self):
        print(f"Transferring {self.path} via S3 to {self.address}:{self.access_key}")
