import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class DlinkCamera(HTTPProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^d-link internet camera", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = self.get_header_field(data, 'server')

        if server:
            match_obj = self.re_expr.search(server)

            if match_obj:
                metadata.device.manufacturer = 'Dlink'
                metadata.device.type = 'Camera'

        return metadata
