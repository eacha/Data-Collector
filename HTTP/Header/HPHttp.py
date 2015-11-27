import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class HPHttp(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^HP HTTP SERVER;?(?P<printer>[^;]+)?;?", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = data['server']
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.service.manufacturer = 'HP'
                metadata.service.product = 'HP HTTP Server'
                metadata.device.manufacturer = 'HP'
                metadata.device.type = 'Printer'
        return metadata