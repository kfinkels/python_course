from session2.classes.transfer_adapters.base import TransferAdapterBase


class FTPAdapter(TransferAdapterBase):
    def __init__(self, path, server, port):
        super(FTPAdapter, self).__init__(path)
        self.server = server
        self.port = port

    def transfer(self):
        print(f"Transferring {self.path} via FTP to {self.server}:{self.port}")
