import xmltodict
import lxml.etree


class TreeConverter:
    def __call__(self, data: dict) -> lxml.etree.ElementTree:
        return lxml.etree.fromstring(xmltodict.unparse(data).encode('utf-8'))
