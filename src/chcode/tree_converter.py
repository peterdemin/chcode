import lxml.etree
import xmltodict

from chcode.types import Element


class TreeConverter:
    def __call__(self, data: dict) -> Element:
        return lxml.etree.fromstring(xmltodict.unparse(data).encode('utf-8'))
