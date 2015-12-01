import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class WEBrick(HttpProcess):
    """
    https://en.wikipedia.org/wiki/WEBrick
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^webrick/?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.manufacturer = 'Ruby'
                metadata.service.product = 'WEBrick'
                metadata.service.version = match_obj.group('version')
        return metadata