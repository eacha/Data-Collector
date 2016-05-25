import re


class HTTPPreprocessor(object):
    @staticmethod
    def preprocess(data):
        data['raw_header'] = data.get('header')
        data['raw_index'] = data.get('index')
        data.pop('header', None)
        data.pop('index', None)

        data = HTTPPreprocessor.parse_headers(data)
        data = HTTPPreprocessor.parse_index(data)

        return data

    @staticmethod
    def parse_headers(data):
        header = data.get('raw_header')

        if header:
            parsed_header = dict()

            for key, value in header.iteritems():
                if key == "null":
                    data['status'] = HTTPPreprocessor.sanitize_header_value(value)
                    parsed_header['status_code'] = HTTPPreprocessor.sanitize_header_value(value)
                    continue

                parsed_header[HTTPPreprocessor.sanitize_header_name(key)] = HTTPPreprocessor.sanitize_header_value(
                    value)

            data.pop('header', None)
            data['parse_header'] = parsed_header

        return data

    @staticmethod
    def parse_index(data):
        index = data.get('raw_index')
        if index is None:
            return data

        # scripts
        expr = '.*?<script\s?[.,\s]*?(type\s*?=\s*?\"\s*?.*?javascript.*?\s*?\"\s*?)?[.,\s]*?src\s*?=\s*?\"\s*?(?P<script>.*?)\s*?\"'
        re_expr = re.compile(expr, re.IGNORECASE)

        match = re_expr.findall(index)
        if match:
            script_list = list()
            for elem in match:
                if elem[1] != '':
                    script_list.append(elem[1])
            data['parse_index'] = {'scripts': script_list}

        return data

    @staticmethod
    def sanitize_header_name(header_name):
        return header_name.lower().replace('-', '_')

    @staticmethod
    def sanitize_header_value(header_value):
        return ' '.join(header_value).strip()
