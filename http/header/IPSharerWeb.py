import re
from http.http_process import HTTPProcess

__author__ = 'eduardo'


class IPSharereWeb(HTTPProcess): #TODO Revisar
    """
    Router, modems, cameras, embedded systems, etc
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^ip_sharer web\s?(?P<version>[\d\.]+)?", re.IGNORECASE)

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
                metadata.service.product = 'IP Sharer Web'
                metadata.service.version = match_obj.group('version')

        return metadata
