import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class GeoHttp(HttpProcess):
    """
    http://www.geovision.com.tw
    """

    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^geohttpserver", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.service.manufacturer = 'GeoVision'
                metadata.service.product = 'Geo Http Server'
                metadata.device.manufacturer = 'GeoVision'
                metadata.device_type = 'Camera'
        return metadata



