import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class GenericHttp(HttpProcess):
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^http\s?(server)?\s?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.product = 'Http Server'
                metadata.service.version = match_obj.group('version')
        return metadata