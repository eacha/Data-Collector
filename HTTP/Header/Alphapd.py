import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class Alphapd(HttpProcess):# TODO Remove class not add new information
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^alphapd", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return metadata
        """
        server = data['server']
        if server:
            if self.re_expr.search(server):
                metadata.service.product = 'Alphapd'
        return metadata