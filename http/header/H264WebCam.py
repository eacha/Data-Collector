import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class H264WebCam(HTTPProcess):
    """
    http://www.h264soft.com/es/index.html
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^h264webcam", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'Timhillone'
                metadata.service.product = 'H264 WebCam'
                metadata.device.type = 'Camera'

        return metadata   
