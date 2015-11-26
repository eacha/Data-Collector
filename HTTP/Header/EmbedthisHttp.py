import re
from HTTP.HttpProcess import HttpProcess

__author__ = 'eduardo'


class EmbedthisHttp(HttpProcess):
    """
    https://github.com/embedthis/http
    """
    protocol = 'HTTP'
    subprotocol = 'HEADER'

    re_expr = re.compile("^embedthis[\s-]?http/?(?P<version>[\d\.]+)?", re.IGNORECASE)

    def process(self, data, metadata):
        """
        :param data: dict
        :param metadata: Metadata
        :return Metadata
        """
        server = HttpProcess.getServer(data)
        if server:
            match_obj = self.re_expr.search(server)
            if match_obj:
                metadata.product = 'Embedthis Http'
                metadata.version = match_obj.group('version')
                metadata.device_type = 'Embedded'
        return metadata