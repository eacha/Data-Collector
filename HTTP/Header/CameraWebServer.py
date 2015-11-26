import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class CameraWebServer(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^camera web server", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        """
        server = HttpProcess.getServer(data)
        if server:
            if self.re_expr.search(server):
                metadata.product = 'Camera Web Server'
                metadata.device_type = 'Camera'
        return metadata